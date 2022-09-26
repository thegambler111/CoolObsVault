# subscriber.py
import paho.mqtt.client as mqtt
import threading
import time
import logging
from logging.handlers import QueueHandler
import sys
import os
import yaml
from yaml.loader import SafeLoader

logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.handlers.TimedRotatingFileHandler("log/z2m_monitor.log",when='midnight',backupCount=30),
                logging.StreamHandler(sys.stdout)
                ]
            )


status_update_time = time.time()



def on_connect(client, userdata, flags, rc):
    with open('../zigbee2mqtt/data/configuration.yaml') as f:
         data = yaml.load(f, Loader=SafeLoader)
    base_topic = data['mqtt']['base_topic']
    # print(base_topic)
    logging.info('Connected with result code %s', rc)
    # subscribe, which need to put into on_connect
    # if reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    client.subscribe(base_topic + "/bridge/state")
    logging.info('Sucscribed a topic %s/bridge/state',base_topic)

# the callback function, it will be triggered when receiving messages
def on_message(client, userdata, msg):
    global status_update_time
    # print(msg.payload.decode("utf-8"))
    if "online" in msg.payload.decode("utf-8"):
         status_update_time = time.time()
         logging.info('Received a online message: {%s} with payload: {%s}', msg.topic, msg.payload)

# check the last status_update_time
def check_status_update_time():
    global status_update_time
    s = threading.Timer(60,check_status_update_time)

    current_time = time.time()
    if (current_time - status_update_time) >= 180:
        logging.info('Status_update_time out of date at current_time: %s and last status_update_time:%s', current_time, status_update_time)
        logging.info("Starting to restart zigee2mqtt service")
        # s.cancel()
        os.system("echo 'Vtnet@1812' | sudo -S systemctl restart zigbee2mqtt")
        time.sleep(300)
        # s.start()
        # os.system("Vtnet@1812")
    else:
        # print(f"Check status_update_time OK")
        logging.info("Check status_update_time OK")
    s.start()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send the will message to other clients
client.will_set('raspberry/status', b'{"status": "Off"}')

# create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.connect("171.244.173.204", 1884, 60)

# start check status_update_time
check_status_update_time()

# set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()
