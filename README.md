# thermostat_mqtt_to_sql
This module of the nodemcu-thermostat project takes events from the MQTT topics and stores the info in a database

## ENVIRONMENT VARIABLES

To make it work, is necessary some environment variables:

- MQTT_SERVER: the host of the mqtt broker
- MQTT_PORT: the port of the mqtt broker
- MQTT_KEEPALIVE: the keepalive for the conneciton to the mqtt broker (default 60)
- MQTT_TOPIC_PREFIX: the main mqtt topic
- PG_HOST: the host of the database
- PG_PORT: the port of the database
- PG_DB: the name of the database
- PG_USER: the user to connect to the database
- PG_PASS: the pass of the user of the database

## DATABASE

This module works with a PostgreSQL database. The initial script to create the necesary objects is located in ./sql/initial.sql
