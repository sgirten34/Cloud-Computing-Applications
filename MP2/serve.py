from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def serve():
    
    if request.method == 'POST':
        subprocess.Popen(["python3", "stress_cpu.py"]) 
        hostname = socket.gethostname()
       
    elif request.method == 'GET':
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)