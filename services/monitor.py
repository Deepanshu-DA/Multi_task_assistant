import psutil
from services.speech import speak

class SystemMonitor:
    def report_status(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        battery = psutil.sensors_battery()
        battery_status = battery.percent if battery else 'Unknown'

        speak(f"CPU usage is {cpu} percent. Memory usage is {memory} percent. Battery is at {battery_status} percent.")
