import socket as s

def Main():
    host = '127.0.0.1' # string
    port = 5000 # number

    socket = s.socket()
    socket.connect((host, port))

    message = input("-> ")
    while message != 'q':
        socket.send(message.encode('utf-8'))
        data = socket.recv(1024).decode('utf-8')
        print('received from server:', data)

        message = input('-> ')
    socket.close()

if __name__ == '__main__':
    Main()