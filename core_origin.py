import psutil
import time
import os
def maintenance_check(log_file):
    # If log exceeds 5MB (5 * 1024 * 1024 bytes), reset it
    if os.path.exists(log_file) and os.path.getsize(log_file) > 5242880:
        with open(log_file, "w") as f:
            f.write(f"--- LOG RESET: {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
# --- PARENT MANIFESTO: READ-ONLY RULES ---
# 1. System must remain below 80% CPU.
# 2. Log must be hidden.
# 3. Process must remain "Low Key" (No UI).
# ... inside the while True loop ...
        maintenance_check(".sys_cache_log")

def run_suppressed_engine():
    # Create the Identity Card (PID)
    pid = os.getpid()
    with open("core.pid", "w") as f:
        f.write(str(pid))
    
    print(f"Ghost Engine Active. PID: {pid}")
    print("Closing this window will NOT stop the background task if started with /B.")

    while True:
        cpu = psutil.cpu_percent(interval=5)
        ram = psutil.virtual_memory().percent
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # LOGGING (Hidden System Cache)
        log_entry = f"{timestamp} | CPU: {cpu}% | RAM: {ram}%\n"
        with open(".sys_cache_log", "a") as f:
            f.write(log_entry)
            
        time.sleep(10) # Low frequency = Untraceable signature

if __name__ == "__main__":
    run_suppressed_engine()