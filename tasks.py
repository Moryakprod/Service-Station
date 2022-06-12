import socket
import time

import environ
from invoke import task

env = environ.Env()


def wait_port_is_open(host, port):
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            print("Connected to DB successfully!")
            return False
        time.sleep(1)
        print("Retrying connect to BD!")


@task
def run(c):
    host = env("POSTGRES_HOST")
    port = env.int("POSTGRES_PORT")

    wait_port_is_open(host, port)

    c.run("./manage.py dbshell < DB_dump.sql")
    c.run("./manage.py dbshell > DB_dump.sql")
    c.run("./manage.py makemigrations")
    c.run("./manage.py migrate")
    c.run("./manage.py collectstatic --noinput")
    c.run("./manage.py runserver 0.0.0.0:8000")
