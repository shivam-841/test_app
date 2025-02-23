from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome!</h1><p>Visit <a href='/htop'>/htop</a> for system details.</p>"

@app.route("/htop")
def htop():
    full_name = "Shivam Kumar"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')
    
    top_output = subprocess.getoutput("top -b -n 1 | head -20")
    
    return f"""
    <html>
    <head><title>HTOP</title></head>
    <body>
        <h1>HTOP Endpoint</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

