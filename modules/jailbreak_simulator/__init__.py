"""
Jailbreak Simulator Module
Tests various jailbreak techniques against LLM guardrails
"""

from modules.jailbreak_simulator.simulator import JailbreakSimulator, JailbreakResult
from modules.jailbreak_simulator.jailbreak_templates import (
    JAILBREAK_TEMPLATES,
    get_jailbreak_categories,
    get_jailbreaks_by_category,
    get_jailbreaks_by_severity,
)

__all__ = [
    "JailbreakSimulator",
    "JailbreakResult",
    "JAILBREAK_TEMPLATES",
    "get_jailbreak_categories",
    "get_jailbreaks_by_category",
    "get_jailbreaks_by_severity",
]
