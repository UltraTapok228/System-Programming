import ctypes
import os
import json

# Шаг 4: Описываем структуру в точности как в core.h
class CoreInfo(ctypes.Structure):
    _fields_ = [
        ("pid", ctypes.c_int64),
        ("cpus", ctypes.c_int32),
        ("page_size", ctypes.c_int32),
        ("host", ctypes.c_char * 256)
    ]

# Шаг 3: Загружаем библиотеку
# Строим абсолютный путь к core.dll относительно папки brain
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core", "core.dll"))
core_lib = ctypes.CDLL(dll_path)

# Указываем типы аргументов и возвращаемого значения для страховки
core_lib.core_get_info.argtypes = [ctypes.POINTER(CoreInfo)]
core_lib.core_get_info.restype = ctypes.c_int

def main():
    # Шаг 5: Вызов функции ядра
    info = CoreInfo()
    status = core_lib.core_get_info(ctypes.byref(info))

    if status != 0:
        print(f"Ошибка вызова: {status}")
        return

    # Формируем JSON-ответ
    data = {
        "pid": info.pid,
        "cpus": info.cpus,
        "page_size": info.page_size,
        "host": info.host.decode('utf-8')
    }
    
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()