import socket

def Main():
    host = '127.0.0.1'
    port = 5001 # should be different from server on udp 

    server = ('127.0.0.1', 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        data, adress = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('received from server:', data)
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()