#!/usr/bin/env python3
"""
Model Download Script
Downloads the recommended Phi-3 Mini model
"""

import os
import sys
from pathlib import Path

print("=" * 70)
print("RED TEAM LLM LAB - MODEL DOWNLOADER")
print("=" * 70)

# Get project root
project_root = Path(__file__).parent.parent
models_dir = project_root / "models"
models_dir.mkdir(exist_ok=True)

model_file = models_dir / "phi-3-mini-q4.gguf"

if model_file.exists():
    print(f"\n✓ Model already exists: {model_file}")
    print(f"  Size: {model_file.stat().st_size / (1024**3):.2f} GB")
    sys.exit(0)

print("\n📥 Model Download Instructions")
print("-" * 70)
print("\nThe Phi-3 Mini Q4 model needs to be downloaded manually.")
print("\nOption 1: Download from HuggingFace")
print("  1. Visit: https://huggingface.co/")
print("  2. Search for 'phi-3-mini gguf q4'")
print("  3. Download the Q4 quantized GGUF file")
print(f"  4. Place it in: {models_dir}/phi-3-mini-q4.gguf")

print("\nOption 2: Use huggingface-cli")
print("  pip install huggingface-hub")
print("  huggingface-cli download [model-repo] [filename]")

print("\nOption 3: Use wget (if direct link available)")
print("  wget [model-url] -O models/phi-3-mini-q4.gguf")

print("\n" + "=" * 70)
print("After downloading, run this script again to verify.")
print("=" * 70)
