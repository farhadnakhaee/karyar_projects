import socket
import pygame
import sys
from tic_tac_toe import TicTacToe

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8888)
client_socket.connect(server_address)

tic_tac = TicTacToe()
tic_tac.screen.fill(tic_tac.setting.bg_color)
tic_tac.draw_grid()
tic_tac.draw_shapes()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
