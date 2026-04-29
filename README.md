# 🕵️ Red Team Simulation Tool (Windows)

### 🔐 User Activity Logging & Data Exfiltration Simulator

---

## 📖 Overview

This project is a **secure and educational simulation** of how attackers collect and transmit user activity data.
It is designed to help understand **red team techniques** while maintaining ethical and transparent implementation.

Instead of performing real hidden keylogging, this tool provides a **safe environment** to explore:

* Data collection
* Logging mechanisms
* Controlled data transmission

---

## ✨ Key Features

* 📥 **Activity Logging** — Records user input with timestamps
* 💾 **Local Storage** — Saves logs in structured files
* 🌐 **Data Transmission** — Sends logs to a local server
* 📸 **Screenshot Capture** — Manual screen capture feature
* 🖥️ **GUI Interface** — Clean Windows-friendly interface
* 📊 **Web Dashboard** — View logs via browser (`/logs`)

---

## 🛠️ Tech Stack

| Technology | Purpose            |
| ---------- | ------------------ |
| Python     | Core development   |
| Tkinter    | GUI interface      |
| Flask      | Backend server     |
| Requests   | HTTP communication |
| PyAutoGUI  | Screenshot capture |
| Psutil     | System information |

---

## 📂 Project Structure

```id="5q2z9l"
redteam-advanced/
│── client/
│   │── gui.py
│   │── sender.py
│   │── system_info.py
│
│── server/
│   │── server.py
│
│── logs/
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```id="3aj3lu"
git clone https://github.com/YOUR_USERNAME/redteam-simulator.git
cd redteam-simulator
```

---

### 2️⃣ Install Dependencies

```id="dpxgn7"
pip install -r requirements.txt
```

---

### 3️⃣ Start Server

```id="r52snn"
python server/server.py
```

🌐 Open in browser:
👉 http://127.0.0.1:5000

---

### 4️⃣ Run GUI Client

(Open a new terminal)

```id="h2dxpi"
python client/gui.py
```

---

## 🧪 Usage Guide

* ✏️ Enter text → Click **Log Input**
* 🧠 Click **System Info** → Capture system details
* 📸 Click **Screenshot** → Save screen image
* 📤 Click **Send Logs** → Transmit logs to server

---

## 📊 View Logs Dashboard

Open:

```id="fk1x6n"
http://127.0.0.1:5000/logs
```

---

## 🎯 Learning Outcomes

* Understand **attacker data collection techniques**
* Explore **client-server communication**
* Learn **logging & monitoring concepts**
* Build **red team simulation workflows**
* Improve **defensive cybersecurity awareness**

---

## 🛡️ Detection & Prevention Insights

* Monitor unknown background processes
* Detect unusual outbound network traffic
* Use endpoint detection tools
* Apply firewall and access controls

---

## ⚠️ Disclaimer

This project is strictly for **educational purposes only**.

It does **not perform real hidden keylogging** and must not be used for unauthorized monitoring or malicious activity.

---

## 🚀 Future Enhancements

* 📊 Advanced dashboard (charts & analytics)
* 🔐 Data encryption implementation
* 📄 Export logs as reports
* 🖥️ Convert into standalone Windows executable

---

## 👩‍💻 Author

### Riya 

Cybersecurity Enthusiast | Aspiring Red Teamer

---
