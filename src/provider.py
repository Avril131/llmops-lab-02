"""Provider abstraction for Lab 02."""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.models import LLMResponse


class BaseProvider(ABC):
    """Abstract provider interface."""

    @abstractmethod
    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response for the given prompt."""
        # TODO: implement this abstract method contract.
        # stays abstract on purpose: the contract is "take a prompt, return an
        # LLMResponse", and every concrete provider must supply its own body
        raise NotImplementedError("Subclasses must implement generate().")
