#ifndef GPU_TEST_H
#define GPU_TEST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

// Retorna info da GPU: nome, memória total, usada, carga
int test_gpu(char* buffer, size_t len);

// Teste de stress simples da GPU
int stress_gpu(char* buffer, size_t len);

#ifdef __cplusplus
}
#endif

#endif
