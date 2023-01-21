import os
from contextlib import contextmanager
from psycopg2 import pool

db_pool = pool.SimpleConnectionPool(1, 10,
                                    host=os.environ["PG_HOST"],
                                    database=os.environ["PG_DB"],
                                    user=os.environ["PG_USER"],
                                    password=os.environ["PG_PASS"],
                                    port=int(os.environ["PG_PORT"]))


@contextmanager
def db():
    con = db_pool.getconn()
    cur = con.cursor()
    try:
        yield con, cur
    finally:
        cur.close()
        db_pool.putconn(con)


def save_startup(station_id, msg):
    with db() as (conn, cursor):
        try:
            cursor.execute("INSERT INTO startup (date, message, station_id) VALUES (now(), %s, %s)",
                           (msg, station_id))
            conn.commit()
        except Exception as e:
            print(str(e))


def save_read(station_id, temperature, humidity):
    with db() as (conn, cursor):
        try:
            cursor.execute("INSERT INTO read (date, temperature, humidity, station_id) VALUES (now(), %s, %s, %s)",
                           (temperature, humidity, station_id))
            conn.commit()
        except Exception as e:
            print(str(e))


def save_status(status):
    with db() as (conn, cursor):
        try:
            cursor.execute("INSERT INTO status (date, status) VALUES (now(), %s)",
                           (status,))
            conn.commit()
        except Exception as e:
            print(str(e))


def save_mode(mode):
    with db() as (conn, cursor):
        try:
            cursor.execute("INSERT INTO mode (date, mode) VALUES (now(), %s)",
                           (mode,))
            conn.commit()
        except Exception as e:
            print(str(e))


def save_set(client_id, setted):
    with db() as (conn, cursor):
        try:
            cursor.execute("INSERT INTO setted (date, setted, client_id) VALUES (now(), %s, %s)",
                           (setted, client_id))
            conn.commit()
        except Exception as e:
            print(str(e))
