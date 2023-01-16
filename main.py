#!/usr/bin/env python3

import os
import paho.mqtt.client as mqtt
import handle_messages


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(os.environ["MQTT_TOPIC_PREFIX"] + "/#")


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(topic + " " + payload)
    topic_tokens = msg.topic.split("/")
    method = topic_tokens[1]
    if method == "read":
        station_id = topic_tokens[2]
        handle_messages.handle_read(station_id, payload)
    elif method == "status":
        handle_messages.handle_status(payload)
    elif method == "mode":
        handle_messages.handle_mode(payload)
    elif method == "set":
        station_id = topic_tokens[2]
        handle_messages.handle_set(station_id, payload)
    elif method == "startup":
        station_id = topic_tokens[2]
        handle_messages.handle_startup(station_id, payload)
    else:
        print("unknown method " + method)


def main():
    print("Connecting MQTT")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(os.environ["MQTT_SERVER"],
                   int(os.environ["MQTT_PORT"]), int(os.environ["MQTT_KEEPALIVE"]))
    client.loop_forever()


if __name__ == "__main__":
    main()
