"""
Red Team LLM Lab - Advanced Security Modules
"""

__version__ = "0.1.0"

from modules.prompt_analyzer.analyzer import PromptAnalyzer, PromptAnalysis
from modules.jailbreak_simulator.simulator import JailbreakSimulator, JailbreakResult
from modules.honeypot_agents.honeypot import (
    HoneypotAgent,
    OverlyHelpfulHoneypot,
    PromptLeakHoneypot,
    ConfusedContextHoneypot,
    HoneypotOrchestrator,
)
from modules.backdoor_testing.backdoor_tester import BackdoorTester

__all__ = [
    "PromptAnalyzer",
    "PromptAnalysis",
    "JailbreakSimulator",
    "JailbreakResult",
    "HoneypotAgent",
    "OverlyHelpfulHoneypot",
    "PromptLeakHoneypot",
    "ConfusedContextHoneypot",
    "HoneypotOrchestrator",
    "BackdoorTester",
]
