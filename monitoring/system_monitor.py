import psutil


def system_status():
    print("\nSystem Monitoring\n")

    print(f"CPU Usage: {psutil.cpu_percent()}%")

    memory = psutil.virtual_memory()

    print(f"RAM Usage: {memory.percent}%")

    disk = psutil.disk_usage('/')

    print(f"Disk Usage: {disk.percent}%")


if __name__ == "__main__":
    system_status()