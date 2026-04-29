import platform
import psutil

def get_system_info():
    info = {
        "OS": platform.system(),
        "Version": platform.version(),
        "CPU": platform.processor(),
        "RAM": str(round(psutil.virtual_memory().total / (1024**3), 2)) + " GB"
    }
    return info