import psutil

def test_ram():
    mem = psutil.virtual_memory()
    return {
        "total_gb": round(mem.total / (1024**3), 2),
        "available_gb": round(mem.available / (1024**3), 2)
    }

def test_ram_mb(min_mb=128):
    mem = psutil.virtual_memory()
    available_mb = mem.available // (1024**2)
    return {"available_mb": max(min_mb, available_mb)}

if __name__ == "__main__":
    print(test_ram())
