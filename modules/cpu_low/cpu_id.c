#include "cpu_id.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifdef _WIN32
#include <windows.h>
#include <intrin.h>
#else
#include <unistd.h>
#endif

DLL_EXPORT void get_cpu_brand(char* brand) {
#ifdef _WIN32
    int CPUInfo[4] = {0,0,0,0};
    char CPUBrandString[0x40];
    __cpuid(CPUInfo, 0x80000000);
    unsigned int nExIds = CPUInfo[0];
    memset(CPUBrandString, 0, sizeof(CPUBrandString));
    if (nExIds >= 0x80000004) {
        __cpuid((int*)CPUInfo, 0x80000002);
        memcpy(CPUBrandString, CPUInfo, sizeof(CPUInfo));
        __cpuid((int*)CPUInfo, 0x80000003);
        memcpy(CPUBrandString+16, CPUInfo, sizeof(CPUInfo));
        __cpuid((int*)CPUInfo, 0x80000004);
        memcpy(CPUBrandString+32, CPUInfo, sizeof(CPUInfo));
        strcpy(brand, CPUBrandString);
        return;
    }
#endif
    strcpy(brand, "CPU_UNKNOWN");
}

DLL_EXPORT int get_cpu_logical_cores() {
#ifdef _WIN32
    SYSTEM_INFO sysinfo;
    GetSystemInfo(&sysinfo);
    return sysinfo.dwNumberOfProcessors;
#else
    return sysconf(_SC_NPROCESSORS_ONLN);
#endif
}

DLL_EXPORT int test_cpu_load(int seconds) {
    clock_t start = clock();
    volatile double dummy = 0;
    while ((clock() - start) < seconds * CLOCKS_PER_SEC) {
        for (int i=0; i<1000000; i++) {
            dummy += i * 0.000001;
        }
    }
    return 1; // 1 = teste completado
}
