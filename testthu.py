print("🔧 Đang chạy script testthu.py")

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("✅ Đã kết nối với mã trạng thái: " + str(rc))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"📩 Nhận tin nhắn: {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client()
client.enable_logger()  # Hiện log debug
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_start()
client.publish("test/topic", "Xin chào từ Python!")
client.loop_forever()
