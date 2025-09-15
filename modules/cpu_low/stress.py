import ctypes
import os

libname = os.path.join(os.path.dirname(__file__), "stress.dll")
stress_lib = ctypes.CDLL(libname)

stress_lib.stress_cpu.argtypes = [ctypes.c_int]
stress_lib.stress_cpu.restype = ctypes.c_int

stress_lib.stress_ram.argtypes = [ctypes.c_int, ctypes.c_int]
stress_lib.stress_ram.restype = ctypes.c_int

def stress_cpu(seconds=5):
    return stress_lib.stress_cpu(seconds)

def stress_ram(mb=100, seconds=5):
    return stress_lib.stress_ram(mb, seconds)

if __name__ == "__main__":
    print("CPU Stress Test:", stress_cpu(2))
    print("RAM Stress Test:", stress_ram(50, 2))
