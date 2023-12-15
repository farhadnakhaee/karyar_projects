# Tic Tac Toe Game
The codes of this game are divided into two parts:
 * ## Server side:
   * ### client_handler: 
     It takes the move from the client and applies the changes to the board. Finally it send board to clients.
   * ### server:
     Initialize server and accept two clients. It creates a thread for each client.
   * ### setting:
     A class for settings of game.
* ## Client side:
   * ### client:
      This file is for data that get client from server and send move of client.
   * ### game_renderer:
      Game render is for rendering the game for client. 

