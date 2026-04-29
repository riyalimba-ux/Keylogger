from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Store logs in memory
received_logs = []

# ✅ Home route (no more 404)
@app.route('/')
def home():
    return render_template_string("""
    <h2>🛡️ Red Team Server Dashboard</h2>
    <p>Status: ✅ Running</p>
    <a href="/logs">View Logs</a>
    """)

# ✅ Receive data
@app.route('/receive', methods=['POST'])
def receive():
    data = request.json.get("data")

    print("\n📥 Received Data:\n", data)

    received_logs.append(data)

    return jsonify({"status": "ok"}), 200

# ✅ View logs in browser
@app.route('/logs')
def logs():
    return "<br><br>".join(received_logs)

if __name__ == "__main__":
    print("🚀 Server running on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000)