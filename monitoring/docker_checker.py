import docker

client = docker.from_env()


def check_containers():
    try:
        containers = client.containers.list(all=True)

        print("\nDocker Containers Status\n")

        for container in containers:
            print(
                f"Container: {container.name} | "
                f"Status: {container.status}"
            )

    except Exception as e:
        print("Docker Error:", e)


if __name__ == "__main__":
    check_containers()