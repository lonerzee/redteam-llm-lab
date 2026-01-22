"""
Honeypot Agents Module
Intentionally vulnerable agents to attract and study attacks
"""

from modules.honeypot_agents.honeypot import (
    HoneypotAgent,
    OverlyHelpfulHoneypot,
    PromptLeakHoneypot,
    ConfusedContextHoneypot,
    HoneypotOrchestrator,
)

__all__ = [
    "HoneypotAgent",
    "OverlyHelpfulHoneypot",
    "PromptLeakHoneypot",
    "ConfusedContextHoneypot",
    "HoneypotOrchestrator",
]
