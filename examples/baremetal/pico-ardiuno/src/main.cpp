#include <Arduino.h> 
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define SLAVE_ADDRESS 0x3C
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire);

void oled_setup()
{
    display.begin(SSD1306_SWITCHCAPVCC, SLAVE_ADDRESS);
    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(WHITE);
    display.setCursor(0, 0);
    display.println("  Arduino");
    display.setTextColor(BLACK, WHITE);
    display.println(" Pi Pico  ");
    display.println("  RP2040  ");
    display.setTextSize(1);
    display.setTextColor(WHITE, BLACK);
    display.println();
    display.println("      WizIO 2021");
    display.display();
}

int main(void)
{
    Serial.begin(115200, true);
    pinMode(25, OUTPUT);
    oled_setup();
    while (true)
    {
        Serial.print("LO");
        Serial.println("OP");
        Serial.printf("MILLIS = %u\n", millis());
        printf("PRINTF %f\n", 22.0 / 7);

        static int led = 0;
        digitalWrite(25, led);
        led ^= 1;
        delay(1000);
    }
}
