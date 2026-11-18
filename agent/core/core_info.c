#include "core.h"
#include <windows.h>

int core_get_info(struct core_info *info) {
    // 1. Получаем номер текущего процесса
    info->process_id = GetCurrentProcessId();

    // 2. Получаем данные о процессорах и памяти
    SYSTEM_INFO sys_info;
    GetNativeSystemInfo(&sys_info);
    info->processors_count = sys_info.dwNumberOfProcessors;
    info->page_size = sys_info.dwPageSize;

    // 3. Получаем имя компьютера
    WCHAR w_name[256];
    DWORD name_len = 256;
    
    if (!GetComputerNameW(w_name, &name_len)) {
        // Если произошла ошибка, возвращаем её системный код
        return GetLastError();
    }

    // Конвертируем строку из UTF-16 в обычный массив char (UTF-8)
    WideCharToMultiByte(CP_UTF8, 0, w_name, -1, info->computer_name, 256, NULL, NULL);

    return 0; // 0 означает успех
}