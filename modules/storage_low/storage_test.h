#ifndef STORAGE_TEST_H
#define STORAGE_TEST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

// Testa todos os discos conectados
// Retorna info de cada disco em JSON/texto
int test_storage(char* buffer, size_t len);

// Testa disco específico pelo caminho (ex: "C:/")
// Retorna detalhes de espaço e SMART
int test_storage_disk(const char* disk_path, char* buffer, size_t len);

#ifdef __cplusplus
}
#endif

#endif
