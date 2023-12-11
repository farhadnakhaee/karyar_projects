import socket
import threading


class ChatServer:
    def __init__(self, ip: str, port: int):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen()
        self.clients = []

    def accept(self):
        conn, addr = self.server_socket.accept()
        print(f"client {addr} is connected")
        return conn
    
    def handle_client(self, conn: socket):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode())
            # DO SOME OTHER STUFF HERE
            self.broadcast(data)

    def broadcast(self, data: bytes) -> None:
        for client in self.clients:
            client.send(data)

    def start(self) -> None:
        while True:
            client = self.accept()
            self.clients.append(client)
            client_handler_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_handler_thread.start()


server = ChatServer("127.0.0.1", 54321)
server.start()
