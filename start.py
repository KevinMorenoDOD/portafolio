import os
import subprocess
import sys


def get_port() -> int:
    configured_port = os.getenv("PORT")
    if configured_port:
        return int(configured_port)

    return 3000  # Default Reflex prod port


port = get_port()
print(f"Starting Reflex on port {port}")

# Reflex production mode serves frontend + backend on a single port.
# --frontend-port sets the port for both frontend and backend.
# --backend-host 0.0.0.0 ensures it's accessible from outside the container.
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
