#include <stdio.h>
#include "pico/stdlib.h"

void blink(int ms)
{
    if (0 == gpio_get_dir(PICO_DEFAULT_LED_PIN))
    {
        gpio_init(PICO_DEFAULT_LED_PIN);
        gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);
        printf("[APP] Led init\n");
    }
    gpio_put(PICO_DEFAULT_LED_PIN, 1);
    sleep_ms(ms);
    gpio_put(PICO_DEFAULT_LED_PIN, 0);
    sleep_ms(ms);
}

int main(void)
{
    extern void dap_init(void);
    dap_init(); // run dap ( before all ) cmsis-dap @ core 1

    stdio_init_all();
    printf("\n\n[APP] Raspberry Pi Pico RP2040 CMSIS-DAP 2021 Georgi Angelov\n");
    while (true)
    {
        blink(100);
    }
}
