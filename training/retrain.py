import os
import subprocess
import sys

FLAG_FILE = "monitoring/drift_detected.flag"

if os.path.exists(FLAG_FILE):
    print("⚠ Drift detected → Retraining & registering new model")

    result = subprocess.run(
        [sys.executable, "training/train.py"],
        check=False
    )

    if result.returncode == 0:
        print("✅ Retraining completed successfully")
        os.remove(FLAG_FILE)
    else:
        print("❌ Retraining failed")
