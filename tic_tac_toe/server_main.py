from server_network import Server

server_address = ('localhost', 8888)
server = Server(server_address)
server.connect_to_server()
server.start_game()
print("game started!")

