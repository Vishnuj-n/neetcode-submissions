import subprocess
import sys

choice = input("Setup automatic daily run? (y/n): ")

if choice.lower() == "y":
    subprocess.run([
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", "setup_task.ps1"
    ])
    print("Scheduled task created.")
else:
    print("Skipped setup.")
