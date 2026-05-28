#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "iot";
const char* password = "iotsenai502";

const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

const int ledPin = 4;

void setup_wifi() {
  delay(10);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void callback(char* topic, byte* payload, unsigned int length) {

  String mensagem;

  for (int i = 0; i < length; i++) {
    mensagem += (char)payload[i];
  }

  if (mensagem == "ligado") {
    digitalWrite(ledPin, HIGH);
  }

  if (mensagem == "desligado") {
    digitalWrite(ledPin, LOW);
  }
}

void reconnect() {
  while (!client.connected()) {

    if (client.connect("ESP32Client" , "esp32", "grupo4")) {
      client.subscribe("PROJ/ECOSSISTEMA");
    } else {
      delay(2000);
    }
  }
}

void setup() {

  pinMode(ledPin, OUTPUT);

  setup_wifi();

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }

  client.loop();
}