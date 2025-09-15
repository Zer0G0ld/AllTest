import platform, psutil

def test_cpu():
    cpu_info = {
        "brand": platform.processor(),
        "cores": psutil.cpu_count(logical=False),
        "threads": psutil.cpu_count(logical=True),
        "frequency": psutil.cpu_freq().current
    }
    return cpu_info
