"""Student-facing configuration helpers for Lab 02."""

from __future__ import annotations

import os

DEFAULT_PROVIDER = "mock"


def load_config() -> dict:
    """
    Load configuration from environment variables.

    Expected keys:
    - LLM_PROVIDER
    - OPENAI_API_KEY
    - OPENAI_MODEL
    """
    # TODO: implement this function.
    # read os.environ on every call so tests and the CLI see current values
    return {
        "LLM_PROVIDER": os.environ.get("LLM_PROVIDER", DEFAULT_PROVIDER).strip().lower()
        or DEFAULT_PROVIDER,
        "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY", "").strip(),
        "OPENAI_MODEL": os.environ.get("OPENAI_MODEL", "").strip(),
    }
