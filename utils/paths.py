"""
Path utilities for RedTeam LLM Lab
Provides cross-platform, flexible path handling
"""

import os
from pathlib import Path


def get_project_root() -> Path:
    """
    Get the project root directory

    Returns:
        Path: Absolute path to project root
    """
    # Get the directory containing this file
    current_file = Path(__file__).resolve()
    # Go up two levels: utils/ -> project root
    project_root = current_file.parent.parent
    return project_root


def get_models_dir() -> Path:
    """Get the models directory path"""
    return get_project_root() / "models"


def get_logs_dir() -> Path:
    """Get the logs directory path"""
    return get_project_root() / "logs"


def get_scripts_dir() -> Path:
    """Get the scripts directory path"""
    return get_project_root() / "scripts"


def get_modules_dir() -> Path:
    """Get the modules directory path"""
    return get_project_root() / "modules"


def get_attack_vectors_dir() -> Path:
    """Get the attack vectors directory path"""
    return get_project_root() / "attack-vectors"


def get_rag_docs_dir() -> Path:
    """Get the RAG documents directory path"""
    return get_project_root() / "rag-docs"


def get_default_model_path() -> Path:
    """Get the default model path"""
    return get_models_dir() / "phi-3-mini-q4.gguf"


def get_attack_vectors_file() -> Path:
    """Get the prompt injections file path"""
    return get_attack_vectors_dir() / "prompt_injections.txt"


def ensure_dir_exists(path: Path) -> None:
    """
    Ensure a directory exists, create if it doesn't

    Args:
        path: Directory path to check/create
    """
    path.mkdir(parents=True, exist_ok=True)


# Backward compatibility - convert to string if needed
def get_project_root_str() -> str:
    """Get project root as string (for backward compatibility)"""
    return str(get_project_root())


def get_models_dir_str() -> str:
    """Get models directory as string"""
    return str(get_models_dir())


def get_logs_dir_str() -> str:
    """Get logs directory as string"""
    return str(get_logs_dir())


def get_default_model_path_str() -> str:
    """Get default model path as string"""
    return str(get_default_model_path())
