import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
porta = 1883
topico = "PROJ/ECOSSISTEMA"

client = mqtt.Client()
client.connect(broker, 1833)

while True:
    comando = input("Digite ligado ou desligado: ")

    client.publish(topico, comando)
    print("Mensagem enviada!")