import os
from datetime import datetime
from system_info import get_system_info
from sender import send_data

LOG_FILE = "logs/activity.txt"

def ensure_logs():
    if not os.path.exists("logs"):
        os.makedirs("logs")

def log_data(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {data}\n")

def main():
    ensure_logs()

    print("🕵️ Advanced Activity Simulator (Windows)")
    print("Commands: info | send | exit\n")

    while True:
        user_input = input(">> ")

        if user_input == "exit":
            break

        elif user_input == "info":
            info = get_system_info()
            log_data(str(info))
            print("✅ System info logged")

        elif user_input == "send":
            with open(LOG_FILE, "r") as f:
                send_data(f.read())

        else:
            log_data(user_input)

if __name__ == "__main__":
    main()