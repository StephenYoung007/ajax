from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
    send_from_directory,
)
import socket


app = Flask(__name__)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 8080

value = ''

# network = '192.168.8.116'
network = '192.168.8.255'
def data():
    while True:
        s.bind(('', PORT))
        while True:
            data, address = s.recvfrom(65535)
            value = data
            print('Server received from {}:{}'.format(address, data.decode('utf-8')))


@app.route('/')
def hello_world():
    return value


import time




if __name__ == '__main__':
    data()
    app.run()
