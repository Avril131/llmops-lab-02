"""Optional OpenAI provider implementation for Lab 02."""

from __future__ import annotations

from src.models import LLMResponse
from src.provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """Provider implementation backed by the OpenAI Python SDK."""

    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response using the OpenAI SDK."""
        # TODO: implement this method.
        # imported here so mock mode never needs the SDK installed
        from openai import OpenAI, OpenAIError

        client = OpenAI(api_key=self.api_key)

        try:
            completion = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
        except OpenAIError as exc:
            # only the exception type is reported; the message could quote the
            # request and the request carries the api key
            raise RuntimeError(
                f"openai request failed ({type(exc).__name__})"
            ) from None

        choice = completion.choices[0]
        usage = completion.usage
        return LLMResponse(
            text=(choice.message.content or "").strip(),
            provider="openai",
            model=completion.model or self.model,
            usage={
                "prompt_tokens": usage.prompt_tokens,
                "completion_tokens": usage.completion_tokens,
                "total_tokens": usage.total_tokens,
            }
            if usage
            else None,
        )
