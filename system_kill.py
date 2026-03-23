import os
import signal
import subprocess

def decommission_suite():
    print("--- KINETIC-ODE V2.0 DECOMMISSIONING ---")

    # This command finds and kills all hidden 'pythonw' processes
    # /F = Force, /T = Tree (kills child processes), /IM = Image Name
    try:
        subprocess.run(["taskkill", "/F", "/IM", "pythonw.exe", "/T"], capture_output=True)
        print("[SUCCESS] All Hidden Nodes (Heart & Shield) have been neutralized.")
    except Exception as e:
        print(f"[ERROR] Could not verify node status: {e}")

    # Optional: Clean up the Identity Card
    if os.path.exists("core.pid"):
        os.remove("core.pid")
        print("[CLEANUP] core.pid removed.")

if __name__ == "__main__":
    decommission_suite()