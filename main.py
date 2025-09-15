#from modules import cpu, ram, gpu, storage
from modules.cpu_low import cpu as cpu_low
from modules.ram_low import ram as ram_low
from modules.gpu_low import gpu as gpu_low
from modules.storage_low import storage as storage_low
from datetime import datetime
import json, os, ctypes

libname = os.path.join(os.path.dirname(__file__), "modules", "cpu_low", "cpu_id.dll")
cpu_lib = ctypes.CDLL(libname)


def run_all_tests():
    results = {
        "timestamp": str(datetime.now()),
        "CPU": {
            "high_level": cpu_low.test_cpu(),
            "low_level": cpu_low.get_cpu_brand()
        },
        "RAM": {
            "high_level": ram_low.test_ram(),
            "low_level": ram_low.test_ram_mb(128)
        },
        "GPU": gpu_low.test_gpu(),
        "Storage": {
            "high_level": storage_low.test_storage(),
            "low_level": storage_low.test_storage()
        }
    }
    return results

def save_results(results):
    os.makedirs("data", exist_ok=True)
    filename = f"data/test_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    return filename

def generate_report(results):
    os.makedirs("reports", exist_ok=True)
    report_file = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(report_file, "w") as f:
        f.write("<html><body>")
        f.write("<h1>Relatório de Teste - AllTest</h1>")
        for key, value in results.items():
            f.write(f"<h2>{key}</h2><pre>{value}</pre>")
        f.write("</body></html>")
    return report_file

if __name__ == "__main__":
    results = run_all_tests()
    json_file = save_results(results)
    report_file = generate_report(results)
    print(f"Resultados salvos em {json_file}")
    print(f"Relatório gerado em {report_file}")
