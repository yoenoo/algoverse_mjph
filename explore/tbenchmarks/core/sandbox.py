"""
Docker-based sandbox for isolated LLM code execution.

Provides complete isolation from host system, ensuring LLM code
cannot affect the benchmarking environment.
"""

import docker
from pathlib import Path
import tempfile
import shutil
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class DockerSandbox:
    """
    Docker-based sandbox for isolated LLM code execution.
    
    Creates a temporary container, copies files into it, executes code,
    and copies results back - completely isolated from host system.
    """
    
    def __init__(self, image: str = "algoverse-tbenchmark:latest"):
        """
        Args:
            image: Docker image to use (defaults to custom benchmark image)
        """
        try:
            self.client = docker.from_env()
        except docker.errors.DockerException as e:
            raise RuntimeError(
                f"Docker not available. Make sure Docker is installed and running. Error: {e}"
            )
        
        self.image = image
        self.container = None
        self.container_name = f"algoverse_sandbox_{id(self)}"
        self.work_dir = Path("/workspace")  # Inside container
        self.host_temp_dir = None  # Temporary directory on host
        self._command_history: List[Dict[str, Any]] = []
    
    def create(self) -> Path:
        """
        Create and start a Docker container.
        
        Returns:
            Path to working directory inside container
        """
        # Create temporary directory on host for file transfer
        self.host_temp_dir = Path(tempfile.mkdtemp(prefix="algoverse_sandbox_"))
        logger.debug(f"Created host temp directory: {self.host_temp_dir}")
        
        # Check if image exists, raise error if not
        try:
            self.client.images.get(self.image)
            logger.debug(f"Using existing image: {self.image}")
        except docker.errors.ImageNotFound:
            logger.error(f"Image not found locally: {self.image}")
            raise RuntimeError(
                f"Docker image '{self.image}' not found. "
                f"Please build it first: docker build -t {self.image} -f explore/tbenchmarks/Dockerfile ."
            )
        
        # Create and start container
        try:
            self.container = self.client.containers.run(
                image=self.image,
                name=self.container_name,
                detach=True,  # Run in background
                volumes={
                    str(self.host_temp_dir): {
                        'bind': str(self.work_dir),
                        'mode': 'rw'  # Read-write for copying files
                    }
                },
                working_dir=str(self.work_dir),
                command="tail -f /dev/null",  # Keep container running
                remove=False,  # Don't auto-remove when stopped
                tty=False,  # No interactive terminal
            )
            logger.debug(f"Created container: {self.container_name}")
        except docker.errors.APIError as e:
            raise RuntimeError(f"Failed to create Docker container: {e}")
        
        return self.work_dir
    
    def write_file(self, file_path: str, content: str):
        """
        Write a file directly to the container.
        
        Args:
            file_path: Path relative to work_dir in container
            content: File content as string
        """
        if not self.container:
            raise RuntimeError("Container not created. Call create() first.")
        
        # Write to host temp dir (shared with container via volume)
        full_path = self.host_temp_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content)
        logger.debug(f"Wrote file to container: {file_path}")
    
    def read_file(self, file_path: str) -> str:
        """
        Read a file from the container.
        
        Args:
            file_path: Path relative to work_dir in container
        
        Returns:
            File content as string
        """
        if not self.container:
            raise RuntimeError("Container not created. Call create() first.")
        
        # Read from host temp dir (shared with container via volume)
        full_path = self.host_temp_dir / file_path
        if not full_path.exists():
            raise FileNotFoundError(f"File not found in container: {file_path}")
        
        return full_path.read_text()
    
    def execute_command(
        self, 
        command: str, 
        timeout: int = 30,
        log_command: bool = True
    ) -> Dict[str, Any]:
        """
        Execute command inside container.
        
        Args:
            command: Command to execute (e.g., "python test.py")
            timeout: Timeout in seconds
            log_command: Whether to log this command in history
        
        Returns:
            Dict with stdout, stderr, returncode
        """
        if not self.container:
            raise RuntimeError("Container not created. Call create() first.")
        
        # Refresh container reference (might have been updated)
        try:
            self.container.reload()
        except docker.errors.NotFound:
            raise RuntimeError("Container was stopped or removed")
        
        logger.debug(f"Executing command in container: {command}")
        
        try:
            # Note: exec_run doesn't accept timeout parameter directly
            # Timeout is handled by the Docker daemon or we can use signal-based timeout
            result = self.container.exec_run(
                command,
                workdir=str(self.work_dir)
            )
            
            output = result.output.decode('utf-8', errors='replace')
            returncode = result.exit_code
            
            # Log command in history
            if log_command:
                self._command_history.append({
                    "command": command,
                    "stdout": output,
                    "returncode": returncode,
                    "timestamp": None  # Could add timestamp if needed
                })
            
            return {
                "stdout": output,
                "stderr": "",  # exec_run doesn't separate stderr easily
                "returncode": returncode
            }
        except Exception as e:
            logger.error(f"Error executing command '{command}': {e}")
            raise
    
    def get_file_snapshot(self) -> Dict[str, str]:
        """
        Get snapshot of all files in container work directory.
        
        Returns:
            Dict mapping file paths to file contents
        """
        if not self.container:
            raise RuntimeError("Container not created. Call create() first.")
        
        files = {}
        
        # List all files recursively
        result = self.execute_command(
            f"find {self.work_dir} -type f -not -path '*/.*'",
            log_command=False
        )
        
        if result["returncode"] != 0:
            logger.warning("Failed to list files in container")
            return files
        
        file_paths = [
            line.strip() 
            for line in result["stdout"].split('\n') 
            if line.strip()
        ]
        
        # Read each file
        for file_path in file_paths:
            try:
                # Get relative path
                rel_path = file_path.replace(str(self.work_dir) + '/', '')
                content = self.read_file(rel_path)
                files[rel_path] = content
            except Exception as e:
                logger.warning(f"Failed to read file {file_path}: {e}")
        
        return files
    
    def get_command_history(self) -> List[Dict[str, Any]]:
        """Get history of all commands executed in this sandbox"""
        return self._command_history.copy()
    
    def cleanup(self):
        """Stop and remove container, clean up temp directory"""
        if self.container:
            try:
                self.container.stop(timeout=5)
                self.container.remove()
                logger.debug(f"Removed container: {self.container_name}")
            except docker.errors.NotFound:
                logger.debug(f"Container already removed: {self.container_name}")
            except Exception as e:
                logger.warning(f"Error cleaning up container: {e}")
        
        if self.host_temp_dir and self.host_temp_dir.exists():
            shutil.rmtree(self.host_temp_dir, ignore_errors=True)
            logger.debug(f"Cleaned up temp directory: {self.host_temp_dir}")

