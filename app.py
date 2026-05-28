from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import paho.mqtt.client as mqtt

app = FastAPI()

# CONFIGURAÇÃO MQTT
broker = "192.168.0.65"
porta = 1883
topico = "PROJ/ECOSSISTEMA"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker, porta)

# PASTAS
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


# PÁGINA PRINCIPAL
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# PÁGINA OUTRO BROKER
@app.get("/outrobroker", response_class=HTMLResponse)
async def outrobroker(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="outro_broker.html"
    )


# LIGAR LED
@app.post("/ligar")
def ligar():

    client.publish(topico, "ON")

    return {"mensagem": "LED ligado"}


# DESLIGAR LED
@app.post("/desligar")
def desligar():

    client.publish(topico, "OFF")

    return {"mensagem": "LED desligado"}