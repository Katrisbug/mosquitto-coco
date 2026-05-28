from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import paho.mqtt.client as mqtt

app = FastAPI()

broker = "broker.hivemq.com"
topico = "PROJ/ECOSSISTEMA"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker, 1883)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/ligar")
def ligar():

    client.publish(topico, "ligado")

    return {"status": "ligado"}

@app.post("/desligar")
def desligar():

    client.publish(topico, "desligado")

    return {"status": "desligado"}