def test_gpu():
    # Apenas um mock simples para GPU
    # Se quiser, pode integrar com 'GPUtil' ou 'py3nvml' para NVIDIA
    return {
        "name": "GPU genérica",
        "vram_gb": 2
    }

if __name__ == "__main__":
    print(test_gpu())
