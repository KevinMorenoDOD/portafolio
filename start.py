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

# Render only exposes one public port. `--single-port` makes Reflex build the
# frontend and serve it together with the backend (including the /_event
# websocket) from the same port, which is required for the app to work.
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
        "--single-port",
        "--frontend-port",
        str(port),
    ],
    check=True,
)
