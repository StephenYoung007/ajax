import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 8080

# network = '192.168.8.116'
# network = '192.168.8.255'
if __name__ == '__main__':
#     message = input('please input the message to send\n')
#     ct = time.time()
#     message = message + '(time:' + str(ct) + ')'
#     while True:
#         s.sendto(message.encode('utf-8'), (network, PORT))
#         time.sleep(1)
    s.bind(('', PORT))
    while True:
        data, address = s.recvfrom(65535)
        value = data.decode('utf-8')
        message = value.split('(')[0]
        local_time = time.time()
        remote_time = float(value.split(':')[-1][:-1])
        delay = str((local_time - remote_time)*1000)
        # print(local_time)
        # print(remote_time)
        print('Server received from {}:{} \ndelay:{} ms'.format(address, message, delay))



