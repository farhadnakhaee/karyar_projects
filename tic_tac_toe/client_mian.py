from client_network import Client

server_address = ('localhost', 8888)
client = Client(server_address)
client.start_client()
