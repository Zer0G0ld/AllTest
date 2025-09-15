#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int test_ram(size_t mb) {
    size_t size = mb * 1024 * 1024;
    uint8_t *buffer = (uint8_t*)malloc(size);
    if (!buffer) return -1;

    // Write pattern
    for (size_t i = 0; i < size; i++)
        buffer[i] = 0xAA;

    // Check pattern
    for (size_t i = 0; i < size; i++) {
        if (buffer[i] != 0xAA) {
            free(buffer);
            return i; // posição do erro
        }
    }

    free(buffer);
    return 0; // sucesso
}

int main() {
    int result = test_ram(128); // 128MB teste
    printf("RAM test result: %d\n", result);
    return 0;
}
