import psutil
import time
import csv
from datetime import datetime

TARGET_SCRIPT = "worker.py"
MEMORY_LIMIT_MB = 30.0  # Порог, после которого сработает алерт

print("Мониторинг запущен. Данные сохраняются в log_output.csv...")

# Открываем файл для записи метрик
with open("log_output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "pid", "name", "rss_mb", "cpu_percent", "alert"])

    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'cpu_percent', 'memory_info']):
            try:
                cmdline = proc.info['cmdline']
                
                # Ищем наши процессы
                if cmdline and TARGET_SCRIPT in " ".join(cmdline):
                    pid = proc.info['pid']
                    name = proc.info['name']
                    rss_mb = proc.info['memory_info'].rss / (1024 * 1024)
                    cpu = proc.info['cpu_percent']
                    
                    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                    
                    # Проверяем порог памяти
                    alert = "ПРЕВЫШЕНИЕ ЛИМИТА!" if rss_mb > MEMORY_LIMIT_MB else ""
                    
                    # Выводим в консоль
                    out_msg = f"[{now}] PID: {pid} | CPU: {cpu}% | RSS: {rss_mb:.1f} MB"
                    if alert:
                        out_msg += f" | {alert}"
                    print(out_msg)
                    
                    # Сохраняем строку в CSV
                    writer.writerow([now, pid, name, f"{rss_mb:.1f}", cpu, alert])
                    file.flush()  # Принудительно сбрасываем данные из буфера в файл
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        time.sleep(1)