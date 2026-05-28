#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

const char* WIFI_SSID = "iot";
const char* WIFI_PASSWORD = "iotsenai502";

// IP do computador onde está rodando o Mosquitto
const char* MQTT_BROKER = "192.168.0.65";

const int LED_PIN = 2;

WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length)
{
    String mensagem = "";

    for (unsigned int i = 0; i < length; i++)
    {
        mensagem += (char)payload[i];
    }

    Serial.print("Mensagem recebida: ");
    Serial.println(mensagem);

    if (mensagem == "ON")
    {
        digitalWrite(LED_PIN, HIGH);
    }

    if (mensagem == "OFF")
    {
        digitalWrite(LED_PIN, LOW);
    }
}

void conectarWiFi()
{
    Serial.println("Conectando ao WiFi...");

    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.println("WiFi conectado");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
}

void conectarMQTT()
{
    while (!client.connected())
    {
        Serial.println("Conectando ao MQTT...");

        if (client.connect("ESP32_CLIENT", "esp32", "grupo4"))
        {
            Serial.println("MQTT conectado");

            client.subscribe("PROJ/ECOSSISTEMA");
        }
        else
        {
            Serial.print("Erro: ");
            Serial.println(client.state());

            delay(3000);
        }
    }
}

void setup()
{
    Serial.begin(115200);

    pinMode(LED_PIN, OUTPUT);

    conectarWiFi();

    client.setServer(MQTT_BROKER, 1883);

    client.setCallback(callback);
}

void loop()
{
    if (!client.connected())
    {
        conectarMQTT();
    }

    client.loop();
}