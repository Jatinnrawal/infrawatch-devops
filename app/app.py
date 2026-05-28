from flask import Flask, render_template, jsonify
import psutil
import docker
import subprocess
import os
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "logs/app.log"


def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {message}\n")


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    memory = psutil.virtual_memory()

    return {
        "percent": memory.percent,
        "used": round(memory.used / (1024 ** 3), 2),
        "total": round(memory.total / (1024 ** 3), 2)
    }


def get_disk_usage():
    disk = psutil.disk_usage('/')

    return {
        "percent": disk.percent,
        "used": round(disk.used / (1024 ** 3), 2),
        "total": round(disk.total / (1024 ** 3), 2)
    }


def get_system_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time

    return str(uptime).split('.')[0]


def get_running_processes():
    processes = []

    for process in psutil.process_iter(['pid', 'name']):
        try:
            processes.append(process.info)
        except:
            pass

    return processes[:10]


def get_docker_containers():
    try:
        client = docker.from_env()
        containers = client.containers.list(all=True)

        container_list = []

        for container in containers:
            container_list.append({
                "name": container.name,
                "status": container.status
            })

        return container_list

    except Exception:
        return []


def get_jenkins_status():
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', 'jenkins'],
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

    except Exception:
        return "Unknown"


@app.route('/')
def dashboard():
    data = {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "uptime": get_system_uptime(),
        "containers": get_docker_containers(),
        "jenkins_status": get_jenkins_status(),
        "processes": get_running_processes()
    }

    write_log("Dashboard accessed")

    return render_template('dashboard.html', data=data)


@app.route('/health')
def health_check():
    return jsonify({
        "status": "UP",
        "service": "InfraWatch",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route('/api/stats')
def stats():
    return jsonify({
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage()
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)