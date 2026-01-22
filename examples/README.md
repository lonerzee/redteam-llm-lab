# Examples

This directory contains example scripts and tutorials for using Red Team LLM Lab.

## Quick Start Examples

### 01 - Basic Usage
```bash
python3 examples/01_basic_usage.py
```
Learn how to:
- Analyze prompts for security risks
- Use the protected LLM wrapper
- Interpret risk scores

### 02 - Jailbreak Testing
```bash
python3 examples/02_jailbreak_testing.py
```
Learn how to:
- Test specific jailbreak techniques
- Understand jailbreak categories
- Evaluate guardrail effectiveness

### 03 - Honeypot Deployment
```bash
python3 examples/03_honeypot_deployment.py
```
Learn how to:
- Deploy honeypot agents
- Study attack patterns
- Analyze attacker behavior

## Jupyter Notebooks

For interactive tutorials, check out the notebooks:

```bash
jupyter notebook examples/
```

- `tutorial_01_getting_started.ipynb` - Complete walkthrough
- `tutorial_02_advanced_testing.ipynb` - Advanced techniques
- `tutorial_03_custom_attacks.ipynb` - Build custom attack vectors

## Running Examples

Make sure you have:
1. Installed dependencies: `pip install -r requirements.txt`
2. Downloaded the model to `models/phi-3-mini-q4.gguf`

Then run any example:
```bash
cd redteam-llm-lab
python3 examples/01_basic_usage.py
```

## Next Steps

After trying these examples:
- Run the master dashboard: `python3 scripts/master_dashboard.py`
- Compare protected vs unprotected: `python3 scripts/compare_protected_vs_unprotected.py`
- Run full test suite: `python3 modules/jailbreak_simulator/simulator.py`
