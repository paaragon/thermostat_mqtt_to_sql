from logger import logging as log
import db
import json


def handle_startup(station_id, msg):
    log.info("handle_startup")
    db.save_startup(station_id, msg)


def handle_read(station_id, msg):
    log.info("handle_read " + fixed_quotes)
    fixed_quotes = msg.replace("'", "\"")
    read_info = json.loads(fixed_quotes)
    temperature = read_info["temp"]
    humidity = read_info["hum"]
    db.save_read(station_id, temperature, humidity)


def handle_status(msg):
    log.info("handle_status")
    db.save_status(int(msg))


def handle_mode(msg):
    log.info("handle_mode")
    db.save_mode(msg)


def handle_set(client_id, msg):
    log.info("handle_set")
    db.save_set(client_id, int(msg))
