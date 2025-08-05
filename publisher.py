import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "test/qos"
qos_level = 1

client = mqtt.Client(client_id="QoSPublisher", protocol=mqtt.MQTTv311)

def on_connect(client, userdata, flags, rc):
    print(f"✅ Kết nối thành công với mã trạng thái {rc}")
    message = "🆕 Thử nghiệm lần 2: Đây KHÔNG phải message retained!"
    # Set retain=False rõ ràng
    client.publish(topic, message, qos=qos_level, retain=False)
    print(f"📤 Đã gửi (retain=False): {message}")

client.on_connect = on_connect

client.connect(broker, port)
client.loop_start()
import time; time.sleep(3)
client.loop_stop()
