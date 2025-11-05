"""
Conversation state management for multi-turn LLM interactions.

Tracks conversation history, command execution, and file changes
within a single task. State is maintained within a task but
reset between different tasks/experiments.
"""

from typing import List, Dict, Any
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class ConversationState:
    """
    Manages conversation state within a single task.
    
    State is maintained within a task but reset between tasks.
    """
    
    turns: List[Dict[str, Any]] = field(default_factory=list)
    command_history: List[Dict[str, Any]] = field(default_factory=list)
    file_changes: Dict[str, str] = field(default_factory=dict)  # path -> change_type
    
    def add_turn(
        self, 
        role: str, 
        content: str, 
        metadata: Dict[str, Any] | None = None
    ):
        """
        Add a conversation turn.
        
        Args:
            role: "user", "assistant", or "system"
            content: Message content
            metadata: Additional metadata
        """
        self.turns.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        })
    
    def add_command(
        self,
        command: str,
        stdout: str,
        stderr: str,
        returncode: int,
        metadata: Dict[str, Any] | None = None
    ):
        """
        Add a command to history.
        
        Args:
            command: Command executed
            stdout: Standard output
            stderr: Standard error
            returncode: Return code
            metadata: Additional metadata
        """
        self.command_history.append({
            "command": command,
            "stdout": stdout,
            "stderr": stderr,
            "returncode": returncode,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        })
    
    def track_file_change(self, file_path: str, change_type: str):
        """
        Track a file change.
        
        Args:
            file_path: Path to file
            change_type: "created", "modified", "deleted"
        """
        self.file_changes[file_path] = change_type
    
    def get_messages(self) -> List[Dict[str, str]]:
        """
        Get messages in LLM format.
        
        Returns:
            List of message dicts with "role" and "content"
        """
        return [
            {"role": turn["role"], "content": turn["content"]}
            for turn in self.turns
        ]
    
    def reset(self):
        """Reset state (for new task/experiment)"""
        self.turns.clear()
        self.command_history.clear()
        self.file_changes.clear()
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get summary of conversation state.
        
        Returns:
            Dict with summary statistics
        """
        return {
            "total_turns": len(self.turns),
            "total_commands": len(self.command_history),
            "files_changed": len(self.file_changes),
            "file_changes": self.file_changes.copy(),
        }

