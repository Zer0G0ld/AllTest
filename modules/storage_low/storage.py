import ctypes
import os

if os.name == 'nt':
    libname = 'storage_test.dll'
else:
    libname = './storage_test.so'

storage_lib = ctypes.CDLL(libname)

def test_storage():
    # Apenas roda o main do C via system call
    result = os.system(libname)
    return "PASS" if result == 0 else "FAIL"

if __name__ == "__main__":
    print(test_storage())
