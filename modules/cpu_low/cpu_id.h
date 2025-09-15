#ifndef CPU_ID_H
#define CPU_ID_H

#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

// Obtém o nome da CPU
DLL_EXPORT void get_cpu_brand(char* brand);

// Obtém o número de núcleos lógicos
DLL_EXPORT int get_cpu_logical_cores();

// Teste de carga simples: calcula operações básicas por um tempo
DLL_EXPORT int test_cpu_load(int seconds);

#ifdef __cplusplus
}
#endif

#endif // CPU_ID_H
