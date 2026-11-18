#include "core.h"
#include <stdio.h>

int main(void) {
    // Инициализируем структуру нулями
    struct core_info info = {0}; 
    
    // Передаем адрес структуры в нашу функцию
    int status = core_get_info(&info);

    if (status != 0) {
        printf("Error! Code: %d\n", status);
        return status;
    }

    printf("Process ID: %u\n", info.process_id);
    printf("Processors: %u\n", info.processors_count);
    printf("Page Size:  %u bytes\n", info.page_size);
    printf("Computer:   %s\n", info.computer_name);

    return 0;
}