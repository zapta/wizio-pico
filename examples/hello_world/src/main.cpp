#include <stdio.h>
#include "pico/stdlib.h"
#include "pico.h"

void setup() {
  stdio_init_all();
  gpio_init(PICO_DEFAULT_LED_PIN);
  gpio_set_dir(PICO_DEFAULT_LED_PIN, true);
}

void loop() {
  gpio_put(PICO_DEFAULT_LED_PIN, true);
  sleep_ms(500);
  gpio_put(PICO_DEFAULT_LED_PIN, false);
  sleep_ms(500);
  printf("Hello world\n");
}

int main() {
  setup();
  for (;;) {
    loop();
  }
}
