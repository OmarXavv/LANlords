#include <math.h>
#include "DHT11.h"

const int PIN_NTC = 15;
const int PIN_LDR = 16; 
const int NTC_R25 = 10000;
const int NTC_MATERIAL_CONSTANT = 3950;

void setup() {
    Serial.begin(9600);
}

float get_temperature() {
    int value = analogRead(PIN_NTC); 
    float resistance = (float)value * NTC_R25 / (1024 - value);
    return 1 / (log(resistance / NTC_R25) / NTC_MATERIAL_CONSTANT + 1 / 298.15) - 273.15;
}

float get_humidity() { 
    return DHT11.getHumidity();
}

void loop()
{
    float temperature = get_temperature();
    float humidity = get_humidity();

    // Print temperature, humidity, and brightness to Serial
    Serial.print(temperature);
    Serial.print(",");
    Serial.print(humidity);

    delay(2000);
}