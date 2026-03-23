import subprocess
import os
import time

# --- NODE CONFIGURATION ---
NODES = [
    {"name": "Heart (Performance)", "file": "core_origin.py"},
    {"name": "Shield (Sentinel)", "file": "sentinel_shield.py"}
]

def boot_system():
    print("--- KINETIC-ODE V2.0 ORCHESTRATOR ---")
    for node in NODES:
        print(f"Deploying {node['name']}...")
        # Use 'pythonw' to keep them completely invisible
        subprocess.Popen(["pythonw", node["file"]], creationflags=subprocess.CREATE_NO_WINDOW)
        time.sleep(1)
    print("--- ALL NODES ACTIVE & UNTRACEABLE ---")

if __name__ == "__main__":
    boot_system()