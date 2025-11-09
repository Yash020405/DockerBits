from flask import Flask, render_template_string
import os
import socket
from datetime import datetime

app = Flask(__name__)

# HTML template for the main page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Python Application</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 600px;
            margin: 20px;
        }
        .header {
            color: #333;
            margin-bottom: 30px;
        }
        .info-card {
            background: #f8f9fa;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        .info-label {
            font-weight: bold;
            color: #555;
            display: inline-block;
            width: 120px;
            text-align: left;
        }
        .info-value {
            color: #333;
            font-family: 'Courier New', monospace;
        }
        .success-badge {
            background: #28a745;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            display: inline-block;
            margin: 20px 0;
            font-weight: bold;
        }
        .docker-info {
            background: #e3f2fd;
            border-left-color: #2196f3;
        }
        .assignment-info {
            background: #fff3e0;
            border-left-color: #ff9800;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🐳 DevOps Python Application</h1>
            <div class="success-badge">✅ Container Running Successfully!</div>
        </div>
        
        <div class="info-card">
            <h3>🚀 Application Information</h3>
            <p><span class="info-label">Status:</span> <span class="info-value">Running</span></p>
            <p><span class="info-label">Framework:</span> <span class="info-value">Flask</span></p>
            <p><span class="info-label">Language:</span> <span class="info-value">Python {{ python_version }}</span></p>
            <p><span class="info-label">Timestamp:</span> <span class="info-value">{{ current_time }}</span></p>
        </div>

        <div class="info-card docker-info">
            <h3>🐳 Container Details</h3>
            <p><span class="info-label">Hostname:</span> <span class="info-value">{{ hostname }}</span></p>
            <p><span class="info-label">Port:</span> <span class="info-value">5000</span></p>
            <p><span class="info-label">Environment:</span> <span class="info-value">Dockerized</span></p>
        </div>

        <div class="info-card assignment-info">
            <h3>📚 Assignment Context</h3>
            <p><span class="info-label">Course:</span> <span class="info-value">DevOps Fundamentals</span></p>
            <p><span class="info-label">Topic:</span> <span class="info-value">Docker Containerization</span></p>
            <p><span class="info-label">Demo:</span> <span class="info-value">Custom Image Creation</span></p>
        </div>

        <div style="margin-top: 30px;">
            <h3>🎯 Success Indicators</h3>
            <p>✅ Python application running</p>
            <p>✅ Flask web server active</p>
            <p>✅ Docker container operational</p>
            <p>✅ Port mapping functional</p>
        </div>

        <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee;">
            <p style="color: #666; font-size: 14px;">
                This application demonstrates successful Docker containerization<br>
                for the DevOps assignment (Question 2)
            </p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(
        html_template,
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        hostname=socket.gethostname(),
        python_version="3.x"
    )

@app.route('/health')
def health_check():
    return {
        "status": "healthy",
        "application": "DevOps Python Demo",
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname()
    }

@app.route('/info')
def info():
    return {
        "application": "DevOps Assignment Demo",
        "version": "1.0.0",
        "description": "Python Flask application for Docker containerization demonstration",
        "author": "DevOps Student",
        "assignment": "Question 2 - Docker Implementation",
        "technologies": ["Python", "Flask", "Docker"],
        "endpoints": ["/", "/health", "/info"]
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
