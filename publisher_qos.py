import paho.mqtt.client as mqtt
import time
import sys

# MQTT config
broker = "localhost"
port = 1883
topic = "test/qos"

# Lấy QoS từ dòng lệnh: python publisher_qos.py 1
qos_level = int(sys.argv[1]) if len(sys.argv) > 1 else 0

client = mqtt.Client(client_id="QoSPublisher", protocol=mqtt.MQTTv311)
client.connect(broker, port)
client.loop_start()

print(f"🚀 Sending messages with QoS {qos_level}")
for i in range(1, 11):
    message = f"msg-{i}"
    result = client.publish(topic, message, qos=qos_level)
    status = result[0]
    if status == 0:
        print(f"✅ Sent `{message}` to `{topic}` with QoS {qos_level}")
    else:
        print(f"❌ Failed to send `{message}`")
    time.sleep(0.5)
