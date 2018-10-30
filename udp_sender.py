import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 8080

# network = '192.168.8.116'
# network = '192.168.50.255'
network = 'flask.stephenyoung.top'
if __name__ == '__main__':
    message = input('please input the message to send\n')
    # ct = time.time()
    # message = message + '(time:' + str(ct) + ')'
    while True:
        ct = time.time()
        info = message + '(time:' + str(ct) + ')'
        s.sendto(info.encode('utf-8'), (network, PORT))
        time.sleep(1)
#     s.bind(('', PORT))
#     while True:
#         data, address = s.recvfrom(65535)
#         value = data
#         print('Server received from {}:{}'.format(address, data.decode('utf-8')))



