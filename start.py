import os
import socket
import subprocess
import sys


def get_port() -> int:
    configured_port = os.getenv("PORT")
    if configured_port:
        return int(configured_port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("0.0.0.0", 0))
        return sock.getsockname()[1]


port = get_port()
print(f"Starting Reflex on port {port}")

subprocess.run(
    [
        sys.executable,
        "-m",
        "reflex",
        "run",
        "--env",
        "prod",
        "--backend-host",
        "0.0.0.0",
        "--frontend-port",
        str(port),
    ],
    check=True,
)