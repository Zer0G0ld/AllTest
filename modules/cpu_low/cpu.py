# wrapper.py
import ctypes
import os

# Caminhos completos dos DLLs
CPU_DLL = os.path.join(os.path.dirname(__file__), "cpu_id.dll")
STRESS_DLL = os.path.join(os.path.dirname(__file__), "stress.dll")

# --- CPU ---
cpu_lib = ctypes.CDLL(CPU_DLL)
cpu_lib.get_cpu_brand.argtypes = [ctypes.c_char_p]
cpu_lib.get_cpu_brand.restype = None

def get_cpu_brand():
    brand = ctypes.create_string_buffer(49)
    cpu_lib.get_cpu_brand(brand)
    return brand.value.decode()

# --- STRESS ---
stress_lib = ctypes.CDLL(STRESS_DLL)
stress_lib.cpu_stress.argtypes = [ctypes.c_int]  # Ex: segundos
stress_lib.cpu_stress.restype = None

def stress_cpu(seconds: int):
    stress_lib.cpu_stress(seconds)

if __name__ == "__main__":
    print("CPU Brand:", get_cpu_brand())
    print("Rodando stress CPU por 5 segundos...")
    stress_cpu(5)
    print("Stress finalizado!")
