"""
Red Team LLM Lab - Setup Configuration
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="redteam-llm-lab",
    version="0.1.0",
    author="lonerzee",
    author_email="lonerzee@users.noreply.github.com",
    description="A comprehensive security testing framework for Large Language Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lonerzee/redteam-llm-lab",
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "llama-cpp-python>=0.2.0",
        "numpy>=1.24.0",
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.4.0",
        ],
        "viz": [
            "matplotlib>=3.7.0",
            "seaborn>=0.12.0",
            "pandas>=2.0.0",
        ],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "ipykernel>=6.25.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "redteam-dashboard=scripts.master_dashboard:main",
            "redteam-jailbreak=modules.jailbreak_simulator.simulator:main",
            "redteam-honeypot=modules.honeypot_agents.honeypot:main",
            "redteam-backdoor=modules.backdoor_testing.backdoor_tester:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.yaml", "*.yml", "*.json"],
    },
    zip_safe=False,
    keywords="llm security redteam prompt-injection jailbreak ai-security",
    project_urls={
        "Bug Reports": "https://github.com/lonerzee/redteam-llm-lab/issues",
        "Source": "https://github.com/lonerzee/redteam-llm-lab",
        "Documentation": "https://redteam-llm-lab.readthedocs.io/",
    },
)
