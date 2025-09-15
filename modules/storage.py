import psutil

def test_storage():
    partitions = psutil.disk_partitions()
    disks = []
    for part in partitions:
        usage = psutil.disk_usage(part.mountpoint)
        disks.append({
            "device": part.device,
            "mountpoint": part.mountpoint,
            "fstype": part.fstype,
            "total_gb": round(usage.total / (1024**3), 2),
            "used_gb": round(usage.used / (1024**3), 2),
            "free_gb": round(usage.free / (1024**3), 2),
            "percent_used": usage.percent
        })
    return disks
