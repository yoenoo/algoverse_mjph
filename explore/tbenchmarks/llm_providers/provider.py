"""
Unified LLM provider using OpenRouter.

OpenRouter provides access to multiple LLM providers through a single
OpenAI-compatible API endpoint.

Supports models from:
- OpenAI (openai/gpt-4, openai/gpt-3.5-turbo)
- Anthropic (anthropic/claude-3-opus, anthropic/claude-3-sonnet)
- Google (google/gemini-pro)
- Meta (meta-llama/llama-2-70b-chat)
- And many more...
"""

try:
    from openai import OpenAI
    _HAS_OPENAI = True
except ImportError:
    _HAS_OPENAI = False

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import os
import logging

logger = logging.getLogger(__name__)


@dataclass
class LLMResponse:
    """Normalized response from any LLM provider"""
    text: str
    model: str
    usage: Dict[str, int]  # {"prompt_tokens": 100, "completion_tokens": 50}
    metadata: Dict[str, Any]
    provider: str  # "openrouter"


class LLMProvider:
    """
    Unified LLM provider using OpenRouter.
    
    OpenRouter provides a single API to access multiple LLM providers.
    Uses OpenAI-compatible API format.
    """
    
    def __init__(
        self,
        model: str,
        api_key: Optional[str] = None,
        **kwargs
    ):
        """
        Args:
            model: Model identifier (e.g., "openai/gpt-4", "anthropic/claude-3-opus")
            api_key: OpenRouter API key (if None, tries OPENROUTER_API_KEY env var)
            **kwargs: Additional OpenAI client parameters
        """
        if not _HAS_OPENAI:
            raise ImportError(
                "openai not installed. Install with: pip install openai"
            )
        
        # Get API key from parameter or environment
        if api_key is None:
            api_key = os.getenv("OPENROUTER_API_KEY")
            if not api_key:
                raise ValueError(
                    "OpenRouter API key not found. "
                    "Set OPENROUTER_API_KEY in .env or pass api_key parameter."
                )
        
        self.model = model
        self.api_key = api_key
        
        # Create OpenAI client pointing to OpenRouter
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            **kwargs
        )
    
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        **kwargs
    ) -> LLMResponse:
        """
        Generate a response from the LLM.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional OpenAI API parameters
        
        Returns:
            LLMResponse with normalized response
        """
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        return self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 2000,
        **kwargs
    ) -> LLMResponse:
        """
        Multi-turn chat interface.
        
        Args:
            messages: List of message dicts with "role" and "content"
                     Format: [{"role": "user", "content": "..."}, ...]
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional OpenAI API parameters
        
        Returns:
            LLMResponse with normalized response
        """
        try:
            # Call OpenRouter API (OpenAI-compatible)
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
            
            # Extract response text
            text = response.choices[0].message.content or ""
            
            # Extract usage info
            usage = {}
            if hasattr(response, 'usage') and response.usage:
                usage = {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens,
                }
            else:
                # Fallback: estimate tokens
                total_text = " ".join([msg.get("content", "") for msg in messages])
                usage = {
                    "prompt_tokens": len(total_text.split()),
                    "completion_tokens": len(text.split()),
                    "total_tokens": len(total_text.split()) + len(text.split()),
                }
            
            # Extract metadata
            metadata = {
                "finish_reason": response.choices[0].finish_reason if response.choices else None,
                "model": response.model if hasattr(response, 'model') else self.model,
            }
            
            return LLMResponse(
                text=text,
                model=self.model,
                usage=usage,
                metadata=metadata,
                provider="openrouter"
            )
        
        except Exception as e:
            logger.error(f"Error calling OpenRouter API: {e}")
            raise RuntimeError(f"OpenRouter API call failed: {e}")
    
    @staticmethod
    def create_from_config(
        model: str,
        api_key: Optional[str] = None,
        **kwargs
    ) -> "LLMProvider":
        """
        Create provider from configuration.
        
        Args:
            model: Model name (e.g., "openai/gpt-4", "anthropic/claude-3-opus")
            api_key: OpenRouter API key (if None, tries OPENROUTER_API_KEY env var)
            **kwargs: Additional parameters
        
        Returns:
            LLMProvider instance
        """
        # Get API key from environment if not provided
        if api_key is None:
            api_key = os.getenv("OPENROUTER_API_KEY")
        
        return LLMProvider(
            model=model,
            api_key=api_key,
            **kwargs
        )

