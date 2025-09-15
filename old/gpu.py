try:
    import GPUtil
except:
    GPUtil = None

def test_gpu():
    if GPUtil:
        gpus = GPUtil.getGPUs()
        gpu_info = []
        for gpu in gpus:
            gpu_info.append({
                "name": gpu.name,
                "memory_total": gpu.memoryTotal,
                "memory_used": gpu.memoryUsed,
                "load": gpu.load
            })
        return gpu_info
    else:
        return "GPUtil não instalado ou GPU não detectada"
