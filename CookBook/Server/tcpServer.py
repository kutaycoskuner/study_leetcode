import socket as s

def Main():
    host = '127.0.0.1'
    port = 5000

    socket = s.socket()
    socket.bind((host, port))

    # :: telling socket to listen 1 action at a time
    socket.listen(1)


    client, adress = socket.accept()
    print('connection from:', adress, 'is established')
    while True:
        data = client.recv(1024).decode('utf-8') # bu kadar byte aliyor
        if not data: 
            break
        print('from connected user:', data)
        data = data.upper()
        print('sending: ' + data)
        client.send(data.encode('utf-8'))
    client.close()

if __name__ == '__main__':
    Main()