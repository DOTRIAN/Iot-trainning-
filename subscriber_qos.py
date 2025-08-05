import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "test/qos"
qos_level = 2  # Bạn có thể chỉnh thành 0 hoặc 1 nếu muốn

received_messages = set()

def on_connect(client, userdata, flags, rc):
    print(f"🔌 Connected with result code {rc}")
    client.subscribe(topic, qos=qos_level)
    print(f"📡 Subscribed to `{topic}` with QoS {qos_level}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"📥 Received `{payload}` from `{msg.topic}`")

    if payload in received_messages:
        print(f"⚠️ DUPLICATE message: `{payload}`")
    else:
        received_messages.add(payload)

client = mqtt.Client(client_id="QoSSubscriber", protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()
