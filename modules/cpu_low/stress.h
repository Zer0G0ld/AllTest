#ifndef STRESS_H
#define STRESS_H

#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

// Testa CPU com operações intensivas por X segundos
DLL_EXPORT int stress_cpu(int seconds);

// Testa RAM alocando um buffer e fazendo leitura/escrita por X MB
DLL_EXPORT int stress_ram(int mb, int seconds);

#ifdef __cplusplus
}
#endif

#endif // STRESS_H
