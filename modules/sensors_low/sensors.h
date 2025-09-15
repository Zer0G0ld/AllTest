#ifndef SENSORS_H
#define SENSORS_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

// Retorna info de temperatura, voltagem e bateria CMOS
int test_sensors(char* buffer, size_t len);

// Retorna estado da bateria: presente, carga, saúde
int test_battery(char* buffer, size_t len);

// Testa CMOS: relógio, configuração básica, checksum
int test_cmos(char* buffer, size_t len);

#ifdef __cplusplus
}
#endif

#endif
