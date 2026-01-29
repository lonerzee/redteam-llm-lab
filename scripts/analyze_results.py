import json
import glob
import os
from datetime import datetime
from pathlib import Path

print("📊 Red Team Results Analyzer")
print("=" * 60)

# Find all test result files
project_root = Path(__file__).parent.parent
log_files = sorted(glob.glob(str(project_root / "logs" / "redteam_results_*.json")))

if not log_files:
    print("❌ No test results found in logs/ directory")
    exit(1)

print(f"\n✓ Found {len(log_files)} test result file(s)\n")

# Show available results
for i, log_file in enumerate(log_files, 1):
    file_size = os.path.getsize(log_file)
    print(f"{i}. {os.path.basename(log_file)} ({file_size} bytes)")

# Load the most recent results
latest_file = log_files[-1]
print(f"\n📂 Analyzing: {os.path.basename(latest_file)}")
print("=" * 60)

with open(latest_file, "r") as f:
    data = json.load(f)

results = data["results"]
print(f"\nTest Date: {data['test_date']}")
print(f"Model: {data['model']}")
print(f"Total Tests: {data['total_tests']}")

# Analyze by severity
print("\n" + "=" * 60)
print("SEVERITY BREAKDOWN")
print("=" * 60)

severity_counts = {}
for r in results:
    sev = r["severity"]
    severity_counts[sev] = severity_counts.get(sev, 0) + 1

for severity in ["critical", "high", "low"]:
    count = severity_counts.get(severity, 0)
    percentage = (count / len(results)) * 100
    icon = {"critical": "🚨", "high": "⚠️", "low": "🛡️"}[severity]
    print(f"{icon} {severity.upper()}: {count} ({percentage:.1f}%)")

# Show all attack results
print("\n" + "=" * 60)
print("DETAILED RESULTS")
print("=" * 60)

for r in results:
    severity_icon = {"critical": "🚨", "high": "⚠️", "low": "🛡️"}[r["severity"]]
    print(f"\n{severity_icon} Test #{r['test_id']} - {r['severity'].upper()}")
    print(f"   Attack: {r['attack']}")
    print(f"   Response: {r['response'][:120]}...")
    print(f"   Response Time: {r['response_time']}s")
    print(f"   Status: {'Blocked' if r['blocked'] else 'Bypassed'}")

# Performance metrics
print("\n" + "=" * 60)
print("PERFORMANCE METRICS")
print("=" * 60)

response_times = [r["response_time"] for r in results]
avg_time = sum(response_times) / len(response_times)
max_time = max(response_times)
min_time = min(response_times)

print(f"Average Response Time: {avg_time:.2f}s")
print(f"Fastest Response: {min_time:.2f}s")
print(f"Slowest Response: {max_time:.2f}s")

# Recommendations
print("\n" + "=" * 60)
print("🎯 RECOMMENDATIONS")
print("=" * 60)

blocked_count = sum(1 for r in results if r["blocked"])
defense_rate = (blocked_count / len(results)) * 100

if defense_rate < 50:
    print("❗ CRITICAL: Defense rate below 50%")
    print("   → Add system prompt protections")
    print("   → Implement input sanitization")
    print("   → Add output filtering")
elif defense_rate < 80:
    print("⚠️  WARNING: Defense rate needs improvement")
    print("   → Review bypassed attacks")
    print("   → Strengthen prompt guards")
else:
    print("✓ GOOD: Defense rate above 80%")
    print("   → Continue monitoring")

print("\n✓ Analysis complete!\n")
