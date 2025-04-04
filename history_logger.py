from datetime import datetime

LOG_FILE = "command_history.log"

def log_command(command: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {command}\n")
