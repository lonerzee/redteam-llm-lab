"""
Configuration Loader
Loads and validates configuration from YAML files
"""

import os
import yaml
from typing import Dict, Any
from pathlib import Path


class ConfigLoader:
    """Load and manage configuration from YAML files"""

    DEFAULT_CONFIG_PATH = "config/config.yaml"

    def __init__(self, config_path: str = None):
        """
        Initialize configuration loader.

        Args:
            config_path: Path to config file (default: config/config.yaml)
        """
        if config_path is None:
            # Try to find config relative to this file
            base_dir = Path(__file__).parent.parent
            config_path = base_dir / self.DEFAULT_CONFIG_PATH

        self.config_path = Path(config_path).expanduser()
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, "r") as f:
            config = yaml.safe_load(f)

        return config or {}

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value with dot notation.

        Args:
            key: Configuration key (e.g., 'model.path')
            default: Default value if key not found

        Returns:
            Configuration value or default

        Example:
            >>> config = ConfigLoader()
            >>> model_path = config.get('model.path')
            >>> max_tokens = config.get('generation.max_tokens', 150)
        """
        keys = key.split(".")
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def get_model_config(self) -> Dict[str, Any]:
        """Get model configuration"""
        return self.get("model", {})

    def get_generation_config(self) -> Dict[str, Any]:
        """Get generation configuration"""
        return self.get("generation", {})

    def get_testing_config(self) -> Dict[str, Any]:
        """Get testing configuration"""
        return self.get("testing", {})

    def get_logging_config(self) -> Dict[str, Any]:
        """Get logging configuration"""
        return self.get("logging", {})

    def get_security_config(self) -> Dict[str, Any]:
        """Get security configuration"""
        return self.get("security", {})

    def expand_path(self, path: str) -> str:
        """
        Expand a path relative to project root.

        Args:
            path: Relative or absolute path

        Returns:
            Absolute path
        """
        path = Path(path).expanduser()

        if path.is_absolute():
            return str(path)

        # Make relative to project root
        base_dir = Path(__file__).parent.parent
        return str(base_dir / path)

    def reload(self):
        """Reload configuration from file"""
        self.config = self._load_config()


# Global config instance
_global_config = None


def get_config(config_path: str = None) -> ConfigLoader:
    """
    Get global configuration instance.

    Args:
        config_path: Path to config file (only used on first call)

    Returns:
        ConfigLoader instance
    """
    global _global_config

    if _global_config is None:
        _global_config = ConfigLoader(config_path)

    return _global_config


# Example usage
if __name__ == "__main__":
    config = ConfigLoader()

    print("Model Configuration:")
    print(f"  Path: {config.get('model.path')}")
    print(f"  Context: {config.get('model.n_ctx')}")

    print("\nGeneration Configuration:")
    print(f"  Max Tokens: {config.get('generation.max_tokens')}")
    print(f"  Temperature: {config.get('generation.temperature')}")

    print("\nExpanded Paths:")
    print(f"  Model: {config.expand_path(config.get('model.path'))}")
    print(f"  Logs: {config.expand_path(config.get('logging.dir'))}")
