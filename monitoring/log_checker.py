LOG_FILE = "logs/app.log"


def read_logs():
    try:
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()

        print("\nRecent Logs:\n")

        for log in logs[-10:]:
            print(log.strip())

    except FileNotFoundError:
        print("Log file not found")


if __name__ == "__main__":
    read_logs()