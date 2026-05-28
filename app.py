from fastapi import FastAPI
import paho.mqtt.publish as publish

app = FastAPI()

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

@app.get("/")
def home():
    return {"status": "Servidor funcionando"}

@app.get("/ligar")
def ligar():

    publish.single(
        topic="PROJ/ECOSSISTEMA",
        payload="ON",
        hostname=MQTT_BROKER,
        port=MQTT_PORT
    )

    return {"PROJ/ECOSSISTEMA": "ligado"}

@app.get("/desligar")
def desligar():

    publish.single(
        topic="PROJ/ECOSSISTEMA",
        payload="OFF",
        hostname=MQTT_BROKER,
        port=MQTT_PORT
    )

    return {"PROJ/ECOSSISTEMA": "desligado"}