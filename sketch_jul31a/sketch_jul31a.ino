#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified();

const char* ssid = ""; // nome rede wifi
const char* password = ""; // senha rede wifi
IPAddress serverIP(192, 168, 1, 100);
const int serverPort = 8888;
String x,y,z,s;

WiFiServer server(serverPort);

void setup() {
  Serial.begin(115200);
  if(!accel.begin())   // if ASXL345 sensor not found
  {
    Serial.println("ADXL345 não detectado");
    while(1);
  }
  Serial.println("ADXL345 detectado");

  // Conecta-se à rede Wi-Fi
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }

  server.begin();
  Serial.print("Servidor iniciado em: ");
  Serial.print(WiFi.localIP());
  Serial.print(":");
  Serial.println(serverPort);
}

void loop() {
  // Envia dados para O pc
  WiFiClient client = server.available();
  sensors_event_t event;
  if (client) {
    accel.getEvent(&event);
    x = event.acceleration.x;
    y = event.acceleration.y;
    z = event.acceleration.z;
    s = x +" "+ y +" "+ z;
    client.print(s);
    client.stop();
  }
}