
#!/usr/bin/env python3
import os
import json
import glob
from datetime import datetime
from pathlib import Path

# Get project root
project_root = Path(__file__).parent.parent

def print_header():
    print("\n" + "=" * 80)
    print("🔴 RED TEAM LLM LAB - DASHBOARD")
    print("=" * 80)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

def check_lab_status():
    print("\n📋 LAB COMPONENTS STATUS")
    print("-" * 80)

    components = {
        "Models": project_root / "models" / "phi-3-mini-q4.gguf",
        "Attack Vectors": project_root / "attack-vectors" / "prompt_injections.txt",
        "Legitimate Docs": project_root / "rag-docs" / "legitimate",
        "Poisoned Docs": project_root / "rag-docs" / "poisoned",
        "Test Scripts": project_root / "scripts",
        "Logs": project_root / "logs"
    }

    for name, path in components.items():
        status = "✓" if path.exists() else "✗"
        print(f"{status} {name:20s} - {str(path)}")

def show_test_results():
    print("\n📊 LATEST TEST RESULTS")
    print("-" * 80)

    # Find latest comparison result
    comparison_files = sorted(glob.glob(str(project_root / "logs" / "comparison_*.json")))
    
    if comparison_files:
        with open(comparison_files[-1], 'r') as f:
            data = json.load(f)
        
        results = data['results']
        unprotected_blocked = sum(1 for r in results if r['unprotected_blocked'])
        protected_blocked = sum(1 for r in results if r['protected_blocked'])
        improved = sum(1 for r in results if r['improved'])
        total = len(results)
        
        print("\n🔓 UNPROTECTED MODEL:")
        print(f"   Defense Rate: {(unprotected_blocked/total)*100:.1f}%")
        print(f"   Attacks Blocked: {unprotected_blocked}/{total}")
        
        print("\n🔒 PROTECTED MODEL:")
        print(f"   Defense Rate: {(protected_blocked/total)*100:.1f}%")
        print(f"   Attacks Blocked: {protected_blocked}/{total}")
        
        improvement = ((protected_blocked - unprotected_blocked) / total) * 100
        print(f"\n📈 IMPROVEMENT:")
        print(f"   +{improvement:.1f}% defense rate increase")
        print(f"   {improved} additional attacks blocked")
    else:
        print("\n⚠️  No comparison tests found. Run: python3 scripts/compare_protected_vs_unprotected.py")

def show_attack_library():
    print("\n🎯 ATTACK VECTOR LIBRARY")
    print("-" * 80)

    attack_file = project_root / "attack-vectors" / "prompt_injections.txt"
    if attack_file.exists():
        with open(attack_file, 'r') as f:
            attacks = [line.strip() for line in f if line.strip()]
        
        print(f"\nTotal Attack Patterns: {len(attacks)}")
        print("\nSample Attacks:")
        for i, attack in enumerate(attacks[:3], 1):
            print(f"  {i}. {attack[:65]}...")
    else:
        print("\n⚠️  Attack vector file not found")

def show_available_commands():
    print("\n🛠️  AVAILABLE COMMANDS")
    print("-" * 80)
    
    commands = {
        "Test unprotected model": "python3 scripts/red_team_test_v2.py",
        "Test protected model": "python3 scripts/protected_llm.py",
        "Compare both models": "python3 scripts/compare_protected_vs_unprotected.py",
        "Test RAG poisoning": "python3 scripts/test_rag_poisoning.py",
        "Analyze results": "python3 scripts/analyze_results.py",
        "Show dashboard": "python3 scripts/lab_dashboard.py"
    }
    
    for name, command in commands.items():
        print(f"\n{name}:")
        print(f"  $ {command}")

def show_recommendations():
    print("\n💡 NEXT STEPS & RECOMMENDATIONS")
    print("-" * 80)
    
    print("""
1. 🔄 Expand Attack Vectors
   - Add more injection patterns to attack-vectors/prompt_injections.txt
   - Test jailbreak techniques (DAN, roleplay)
   - Add multi-turn conversation attacks

2. 🧪 Advanced RAG Testing
   - Test indirect prompt injection via documents
   - Simulate document poisoning at scale
   - Test retrieval ranking manipulation

3. 📊 Monitoring & Logging
   - Set up automated testing schedules
   - Create metrics dashboards
   - Track defense rate over time

4. 🔐 Enhance Defenses
   - Add more detection patterns to protected_llm.py
   - Implement semantic similarity checks
   - Add rate limiting and anomaly detection

5. 🌐 Production Readiness
   - Add API endpoints for your protected LLM
   - Implement proper authentication
   - Set up Docker containers for deployment
    """)

def main():
    print_header()
    check_lab_status()
    show_test_results()
    show_attack_library()
    show_available_commands()
    show_recommendations()
    
    print("\n" + "=" * 80)
    print("✓ Dashboard complete!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
