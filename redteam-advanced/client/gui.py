import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import os

from system_info import get_system_info
from sender import send_data

LOG_FILE = "logs/activity.txt"


# ✅ Ensure logs folder exists
def ensure_logs():
    if not os.path.exists("logs"):
        os.makedirs("logs")


# ✅ Logging function
def log_data(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {data}\n")

    output_box.insert(tk.END, f"[{timestamp}] {data}\n")
    output_box.see(tk.END)


# ✅ Input logger
def collect_input():
    user_input = input_entry.get()

    if not user_input.strip():
        log_data("⚠️ Empty input ignored")
        return

    log_data(user_input)
    input_entry.delete(0, tk.END)


# ✅ System info
def show_system_info():
    try:
        info = get_system_info()
        log_data(str(info))
    except Exception as e:
        log_data(f"❌ System info error: {e}")


# ✅ FIXED SEND LOGS FUNCTION
def send_logs():
    try:
        if not os.path.exists(LOG_FILE):
            log_data("❌ Log file not found!")
            return

        with open(LOG_FILE, "r") as f:
            data = f.read()

        if not data.strip():
            log_data("⚠️ Log file is empty")
            return

        print("📡 Sending data...")
        send_data(data)

        log_data("✅ Logs sent successfully!")

    except Exception as e:
        log_data(f"❌ Send error: {e}")


# ✅ FIXED SCREENSHOT FUNCTION
def take_screenshot():
    try:
        import pyautogui

        screenshot_path = "logs/screenshot.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)

        log_data(f"📸 Screenshot saved: {screenshot_path}")

    except Exception as e:
        log_data(f"❌ Screenshot error: {e}")


# ---------------- GUI ---------------- #

ensure_logs()

root = tk.Tk()
root.title("🕵️ Red Team Simulator (Windows)")
root.geometry("650x500")

# Input field
input_entry = tk.Entry(root, width=60)
input_entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Log Input", command=collect_input).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="System Info", command=show_system_info).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Send Logs", command=send_logs).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Screenshot", command=take_screenshot).grid(row=0, column=3, padx=5)

# Output box
output_box = scrolledtext.ScrolledText(root, width=80, height=20)
output_box.pack(pady=10)

root.mainloop()