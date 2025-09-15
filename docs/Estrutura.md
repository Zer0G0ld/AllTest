## **1️⃣ Estrutura do AllTest Nível Raiz**

```bash
AllTest/
│
├─ modules/
│    ├─ cpu_low/         # Testes detalhados de CPU
│    │     ├─ cpu_id.c   # CPUID, frequências, instruções suportadas
│    │     ├─ stress.c   # Stress e cálculo FPU
│    │     └─ cpu.py     # Wrapper Python para chamar C
│    │
│    ├─ ram_low/         # Testes detalhados de RAM
│    │     ├─ mem_test.c # Write/read patterns, erros, latência
│    │     └─ ram.py     # Wrapper Python
│    │
│    ├─ gpu_low/         # Testes de GPU
│    │     ├─ gpu_info.c # PCI enumeration
│    │     └─ gpu.py
│    │
│    ├─ storage_low/     # NVMe/HDD/SSD testes
│    │     ├─ nvme_test.c # SMART, throughput, IO stress
│    │     └─ storage.py
│    │
│    └─ sensors_low/     # Temperatura, voltagem, bateria CMOS
│          ├─ sensors.c
│          └─ sensors.py
│
├─ main.py               # Orquestrador dos módulos
├─ reports/              # Relatórios HTML detalhados
├─ data/                 # JSON de logs
└─ requirements.txt
```

---

## **2️⃣ Estratégia de cada módulo**

### **CPU**

* CPUID → detecta fabricante, modelo, instruções (SSE, AVX, FMA, etc).
* Stress test → cálculos FP intensivos, prime numbers, DGEMM, FFT.
* Frequência → medir frequência base, turbo e flutuações sob carga.
* Erros → detectar travamentos ou instruções falhando.

### **RAM**

* Alocação máxima → detectar limites de memória disponível.
* Write/read patterns → `0x00`, `0xFF`, `0xAA`, `0x55`, zeros e uns alternados.
* Latência → medir tempo de leitura/escrita por bloco.
* Erros → registrar qualquer discrepância de leitura.

### **GPU**

* Detectar via PCIe → Vendor, Device ID, memória, clock.
* Stress test → Renderizar buffers em OpenGL/Vulkan e medir desempenho.
* Teste de memória VRAM → Write/read patterns similares a RAM.

### **Storage**

* SMART → saúde do SSD/HDD.
* Throughput → leitura/gravação sequencial e aleatória.
* Latência → medir tempo de resposta de blocos pequenos.
* Teste de integridade → ler blocos aleatórios e verificar consistência.

### **Sensores / CMOS / Bateria**

* Temperaturas CPU, GPU, placa-mãe.
* Voltagens → Vcore, 3.3V, 5V, 12V rails.
* CMOS → status da bateria e hora correta.
* Detectar shutdowns ou erros de energia anteriores.

---

## **3️⃣ Relatórios detalhados**

O relatório deve conter:

* Seção por módulo (CPU, RAM, GPU, Storage, Sensors)
* Status geral: PASS / FAIL
* Valores medidos → frequência, temperatura, latência, throughput
* Detecção de problemas → discrepâncias, falhas ou warnings
* Gráficos → evolução de carga, temperatura, uso de memória
* Sugestões → “RAM OK”, “GPU com uso de 95% do VRAM”, “Bateria CMOS fraca”

Exemplo de saída JSON:

```json
{
  "timestamp": "2025-09-15T12:00:00",
  "CPU": {
    "brand": "Intel Core i5-1235U",
    "cores": 10,
    "threads": 12,
    "frequency": "2.5GHz",
    "stress_test": "PASS"
  },
  "RAM": {
    "total_gb": 8,
    "errors_detected": 0,
    "latency_ns": 90
  },
  "GPU": {
    "name": "Intel UHD Graphics",
    "memory_total": 2,
    "memory_used": 0.5,
    "stress_test": "PASS"
  },
  "Storage": {
    "device": "/dev/nvme0n1",
    "health_percent": 94,
    "throughput_MBps": 2000
  },
  "Sensors": {
    "CPU_temp_C": 45,
    "VRM_voltages": {
        "Vcore": 1.2,
        "5V": 5.01
    },
    "CMOS_battery": "GOOD"
  }
}
```

