import socket 

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print('server started')
    while True:
        data, adress = s.recvfrom(1024)
        data = data.decode('utf-8')

        print("msg received from:", adress)
        print('from connected user:', data)

        data = data.upper()
        print('sending', data)
        s.sendto(data.encode('utf-8'), adress)
    s.close()

if __name__ == '__main__':
    Main()