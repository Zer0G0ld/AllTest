#ifndef RAM_TEST_H
#define RAM_TEST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

// Testa memória RAM total, disponível e realiza stress simples
// buffer recebe JSON/texto detalhado
int test_ram(char* buffer, size_t len);

// Teste de stress de RAM, especificando MB a testar
int test_ram_mb(size_t mb, char* buffer, size_t len);

#ifdef __cplusplus
}
#endif

#endif
