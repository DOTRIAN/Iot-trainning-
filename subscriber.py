import paho.mqtt.client as mqtt

broker = "192.168.1.7"
port = 1883
topic = "warning/fire"

def on_connect(client, userdata, flags, rc):
    print(f"✅ Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"📥 Received `{msg.payload.decode()}` from topic `{msg.topic}`")

client = mqtt.Client(client_id="FireSubscriber", protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

print("⏳ Connecting to broker...")
client.connect(broker, port)
client.loop_forever()
