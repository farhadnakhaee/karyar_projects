# Tic Tac Toe Game

## How to run:
This game is web socket application.
For run game, first install pygame then open 3 terminal:
one for server_main.py and two for client_main.py:
`python3 server_main.py` and `python3 client_main.py`

## Files:
The codes of this game are divided into two parts:
 * ### Server side:
   * server_main: It includes the main class in which client requests are heard and answered according to the protocol
   * server_network: Manage send or receive game state, player symbol, massage and move.
   * game_logic: In this file we manage the game logic for ex: check win or tie. 
   * setting: A class for settings of game.
   
* ### Client side:
   * client_main: It includes the main loop for run the client.
   * client_network: This file is for data that get client from server and send move of client.
   * game_renderer: Game render is for rendering the game for client. 

## How is work:
After two clients connected to server, server listen to client's request and send response to client.
Request of client contains:
```{"action": action, "data": data, "player": player}```
The player is for the server to know from whom the request was sent, so that it can respond to the same.
Finally, server call protocol to response to request. 
