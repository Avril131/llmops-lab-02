"""Student-facing application logic for Lab 02."""

from __future__ import annotations

from src.config import load_config
from src.mock_provider import MockProvider

MAX_PROMPT_CHARS = 10000


def validate_prompt(prompt: str) -> str:
    """Validate and normalize a user prompt."""
    # TODO: implement this function.
    if not isinstance(prompt, str):
        raise TypeError(f"prompt must be a str, got {type(prompt).__name__}")

    cleaned = prompt.strip()
    if not cleaned:
        raise ValueError("prompt must not be empty or whitespace only")
    if len(cleaned) > MAX_PROMPT_CHARS:
        raise ValueError(
            f"prompt is {len(cleaned)} characters, limit is {MAX_PROMPT_CHARS}"
        )

    return cleaned


def create_provider(config: dict):
    """Select and instantiate the configured provider."""
    # TODO: implement this function.
    name = config.get("LLM_PROVIDER", "mock")

    if name == "mock":
        return MockProvider()

    if name == "openai":
        api_key = config.get("OPENAI_API_KEY", "")
        model = config.get("OPENAI_MODEL", "")
        # named without values so the message stays safe to log
        missing = [
            key
            for key, value in (("OPENAI_API_KEY", api_key), ("OPENAI_MODEL", model))
            if not value
        ]
        if missing:
            raise ValueError(f"provider 'openai' needs {', '.join(missing)}")

        # imported lazily so mock mode does not depend on the openai package
        from src.openai_provider import OpenAIProvider

        return OpenAIProvider(api_key=api_key, model=model)

    raise ValueError(f"unknown provider {name!r}, expected 'mock' or 'openai'")


def generate_response(prompt: str) -> dict:
    """Generate a normalized response for a user prompt."""
    # TODO: implement this function.
    cleaned = validate_prompt(prompt)
    provider = create_provider(load_config())
    # provider errors travel up unchanged; the caller decides how to report them
    response = provider.generate(cleaned)
    return {
        "text": response.text,
        "provider": response.provider,
        "model": response.model,
    }


def main() -> None:
    """Simplified CLI entry point for the lab."""
    print("LLMOps Lab 02")

    try:
        config = load_config()
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("Provider:", config.get("LLM_PROVIDER", "mock"))

    prompt = input("\nEnter prompt:\n> ")

    try:
        response = generate_response(prompt)
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return
    except (TypeError, ValueError) as exc:
        print(f"\nInvalid request: {exc}")
        return
    except RuntimeError as exc:
        print(f"\nProvider error: {exc}")
        return

    print("\nResponse:")
    print(response["text"])


if __name__ == "__main__":
    main()
