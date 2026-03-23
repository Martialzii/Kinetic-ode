import os
import shutil
import time

# --- SENTINEL SHIELD: BASE LAYER ---
WATCH_DIR = os.path.expanduser("~/Downloads")
QUARANTINE_DIR = "C:/Users/ADMIN/Desktop/Kinetic-ode/Quarantine"
GENRE = "Sentinel Logic"

def run_shield():
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)
        
    print(f"[{GENRE}] Shield Active. Monitoring: {WATCH_DIR}")

    while True:
        try:
            for file in os.listdir(WATCH_DIR):
                # Intercept binaries and scripts before execution
                if file.lower().endswith((".exe", ".msi", ".bat", ".vbs", ".ps1")):
                    source = os.path.join(WATCH_DIR, file)
                    dest = os.path.join(QUARANTINE_DIR, file)
                    
                    shutil.move(source, dest)
                    
                    with open(".sys_cache_log", "a") as log:
                        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | [ALERT] {GENRE} intercepted {file}\n")
        except Exception as e:
            pass # Stay silent
            
        time.sleep(2) # Faster pulse for security

if __name__ == "__main__":
    run_shield()