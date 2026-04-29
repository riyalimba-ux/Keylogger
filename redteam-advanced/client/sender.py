import requests

SERVER_URL = "http://127.0.0.1:5000/receive"

def send_data(data):
    try:
        print("📡 Sending data to server...")

        response = requests.post(
            SERVER_URL,
            json={"data": data}
        )

        print("✅ Status Code:", response.status_code)

        if response.status_code == 200:
            print("📤 Data sent successfully!")
        else:
            print("❌ Failed to send")

    except Exception as e:
        print("❌ Error:", e)