import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "warning/fire"

def on_connect(client, userdata, flags, rc):
    print(f"✅ [Sub2] Connected with result code {rc}")
    client.subscribe(topic)
    print(f"📡 [Sub2] Subscribed to `{topic}`")

def on_message(client, userdata, msg):
    print(f"📥 [Sub2] Received `{msg.payload.decode()}` from `{msg.topic}`")

# ⚠️ Tên client khác với sub đầu tiên
client = mqtt.Client(client_id="FireSubscriber2", protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

print("⏳ [Sub2] Connecting to broker...")
client.connect(broker, port)
client.loop_forever()
