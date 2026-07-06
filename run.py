import subprocess

subprocess.run([
    "uvicorn",
    "web:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8080"
])