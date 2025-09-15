# **AllTest – Sistema de Teste de Hardware Bare-Metal**

**Versão:** 0.1 – Alpha
**Autor:** Zer0G0ld
**Objetivo:** Ferramenta para testes completos de hardware em PCs, Notebooks e All-in-One, independente do sistema operacional, gerando relatórios em JSON e HTML.

---

## **Descrição**

O AllTest é um sistema modular de diagnóstico de hardware projetado para:

* Detectar e registrar informações de CPU, RAM, GPU e armazenamento.
* Gerar relatórios automáticos em JSON e HTML.
* Rodar tanto em sistemas Windows quanto em Linux Live (bare-metal), sem dependência do SO.
* Servir como base para stress tests, benchmarks e monitoramento de integridade do hardware.

---

## **Funcionalidades da Versão Alpha**

* Detecção de CPU (marca, cores, threads e frequência).
* Detecção de RAM (total, disponível, usada e percentual).
* Detecção de GPU (nome, memória total, usada e carga).
* Detecção de Storage (partições, espaço total, usado, livre e percentual).
* Salva resultados em JSON.
* Gera relatório HTML simples.

---

## **Estrutura do Projeto**

```
AllTest/
│
├─ modules/        # Módulos de teste (CPU, RAM, GPU, Storage)
│    ├─ cpu.py
│    ├─ ram.py
│    ├─ gpu.py
│    └─ storage.py
│
├─ reports/        # Relatórios HTML gerados
├─ data/           # Logs JSON gerados
├─ main.py         # Script principal que roda todos os testes
└─ requirements.txt
```

---

## **Pré-Requisitos**

* Python 3.10 ou superior
* Bibliotecas:

  * psutil
  * GPUtil (opcional para GPU)
  * reportlab / matplotlib (opcional para gráficos)

Instale dependências com:

```bash
pip install -r requirements.txt
```

---

## **Uso**

1. Clone o repositório:

```bash
git clone https://github.com/Zer0G0ld/AllTest.git
cd AllTest
```

2. Rode o script principal:

```bash
python main.py
```

3. Resultados:

* JSON: `data/test_result_YYYYMMDD_HHMMSS.json`
* Relatório HTML: `reports/report_YYYYMMDD_HHMMSS.html`

---

## **Próximos Passos / Roadmap**

* Adicionar **stress tests para CPU, RAM e GPU**.
* Testes de **periféricos (USB, webcam, áudio)**.
* Suporte a **boot em Linux Live** para teste bare-metal.
* Geração de gráficos detalhados no relatório.
* Automação e histórico de máquinas testadas.

---

## **Licença**

[GNU3 LICENSE](LICENSE) – Use, modifique e distribua livremente.
