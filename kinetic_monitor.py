import psutil
import time
from datetime import datetime

def run_tracker():
    print("🚀 KINETIC-ODE: System Efficiency Active")
    print("Press Ctrl+C to stop the monitoring session.\n")
    
    start_time = time.time()
    
    try:
        while True:
            # 1. Engineering Metric: CPU Load (Energy Proxy)
            cpu_usage = psutil.cpu_percent(interval=1)
            # 2. Engineering Metric: RAM Load
            ram_usage = psutil.virtual_memory().percent
            
            # 3. Process Optimization Logic
            status = "OPTIMAL" if cpu_usage < 50 else "ENERGY SPIKE"
            
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] CPU: {cpu_usage}% | RAM: {ram_usage}% | Status: {status}")
            
            # Save to log for later bottleneck analysis
            with open("efficiency_log.txt", "a") as f:
                f.write(f"{timestamp}, {cpu_usage}%, {ram_usage}%\n")
                
            time.sleep(1) 
            
    except KeyboardInterrupt:
        duration = round((time.time() - start_time) / 60, 2)
        print(f"\n✅ Session Ended. Total Time: {duration} mins.")
        print("Data saved to efficiency_log.txt.")

if __name__ == "__main__":
    run_tracker()