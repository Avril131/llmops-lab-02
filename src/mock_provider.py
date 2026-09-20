"""Mock provider for Lab 02."""

from __future__ import annotations

from src.models import LLMResponse
from src.provider import BaseProvider

MOCK_MODEL = "mock-model"


class MockProvider(BaseProvider):
    """Deterministic provider used for testing and local development."""

    def generate(self, prompt: str) -> LLMResponse:
        """Return a deterministic mock response."""
        # TODO: implement this method.
        # echoing the prompt keeps the output deterministic and makes it obvious
        # in a test which request produced which response
        words = len(prompt.split())
        return LLMResponse(
            text=f"Mock response for prompt: {prompt}",
            provider="mock",
            model=MOCK_MODEL,
            usage={
                "prompt_tokens": words,
                "completion_tokens": words + 4,
                "total_tokens": 2 * words + 4,
            },
        )
