import json
from modules import cpu, ram, gpu, storage
from datetime import datetime

def run_tests():
    results = {
        "timestamp": str(datetime.now()),
        "CPU": cpu.test_cpu(),
        "RAM": ram.test_ram(),
        "GPU": gpu.test_gpu(),
        "Storage": storage.test_storage()
    }
    return results

def save_results(results):
    filename = f"data/test_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    return filename

def generate_report(results):
    report_file = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(report_file, "w") as f:
        f.write("<html><body>")
        f.write("<h1>Relatório de Teste - AllTest</h1>")
        for key, value in results.items():
            f.write(f"<h2>{key}</h2><pre>{value}</pre>")
        f.write("</body></html>")
    return report_file

if __name__ == "__main__":
    results = run_tests()
    json_file = save_results(results)
    report_file = generate_report(results)
    print(f"Resultados salvos em {json_file}")
    print(f"Relatório gerado em {report_file}")
