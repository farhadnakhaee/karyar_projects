import socket
import threading


class ChatClient:
    def __init__(self, server_ip: str, server_port: int):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_address = (server_ip, server_port)
        self.name = input("name: ")

    def connect(self):
        self.server_socket.connect(self.server_socket_address)

    def sending_loop(self):
        while True:
            message = input()
            _message = self.name + ": " + message
            self.server_socket.send(_message.encode())

    def receiving_loop(self):   
        while True:   
            data = self.server_socket.recv(1024)
            if not data:
                break
            split_data = data.decode().split(":")
            name = split_data[0]
            if name == self.name:
                data = "me: " + split_data[1]
                print(data)
            else:
                print(data.decode())

    def start(self):
        self.connect()
        sending_loop = threading.Thread(target=self.sending_loop)
        sending_loop.start()
        self.receiving_loop()


client = ChatClient("127.0.0.1", 54321)
client.start()
