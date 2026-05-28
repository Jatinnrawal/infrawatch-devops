import subprocess


def check_jenkins():
    try:
        result = subprocess.run(
            ["systemctl", "is-active", "jenkins"],
            capture_output=True,
            text=True
        )

        status = result.stdout.strip()

        print(f"Jenkins Status: {status}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    check_jenkins()