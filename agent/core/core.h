#pragma once
#include <stdint.h>

struct core_info {
    uint32_t process_id;
    uint32_t processors_count;
    uint32_t page_size;
    char computer_name[256];
};

int core_get_info(struct core_info *info);