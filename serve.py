from flask import Flask, request, jsonify, render_template
import subprocess
import socket
app = Flask(__name__, template_folder='./')

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        # Handle POST request to stress CPU
        print("CPU stress test")
        stress_process = subprocess.Popen(['python', 'stress_cpu.py'])
        return jsonify({'status': 'CPU stress initiated'})

    if request.method == 'GET':
        # Handle GET request to return private IP address
        print("hello")
        private_ip = socket.gethostbyname(socket.gethostname())
        return jsonify({'private_ip': private_ip})

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)