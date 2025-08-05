import paho.mqtt.client as mqtt
import time

# Thông tin broker
broker = "localhost"
port = 1883
topic = "warning/fire"

# Tạo client MQTT
client = mqtt.Client(client_id="FirePublisher", protocol=mqtt.MQTTv311)


# Kết nối tới broker
client.connect(broker, port)

# Gửi dữ liệu mỗi 2 giây
while True:
    message = "🔥 Fire detected!"
    result = client.publish(topic, message)
    status = result[0]

    if status == 0:
        print(f"Sent `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    
    time.sleep(2)
