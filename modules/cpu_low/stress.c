#include "stress.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

DLL_EXPORT int stress_cpu(int seconds) {
    clock_t start = clock();
    volatile double dummy = 0;
    while ((clock() - start) < seconds * CLOCKS_PER_SEC) {
        for (int i = 0; i < 1000000; i++) {
            dummy += i * 0.000001;
        }
    }
    return 1; // sucesso
}

DLL_EXPORT int stress_ram(int mb, int seconds) {
    size_t size = mb * 1024 * 1024;
    char* buffer = (char*)malloc(size);
    if (!buffer) return 0; // falha

    clock_t start = clock();
    while ((clock() - start) < seconds * CLOCKS_PER_SEC) {
        for (size_t i = 0; i < size; i++) {
            buffer[i] = (char)(i % 256);
        }
        for (size_t i = 0; i < size; i++) {
            volatile char c = buffer[i];
        }
    }

    free(buffer);
    return 1; // sucesso
}
