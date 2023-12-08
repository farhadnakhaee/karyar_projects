import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys  # {"i": "UP", "k": "DOWN", "j": "LEFT", "l": "RIGHT"}
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        head = self.get_head()
        new_head_x = self.val(head[0] + self.dx[self.direction])
        new_head_y = self.val(head[1] + self.dy[self.direction])
        new_head = (new_head_x, new_head_y)
        next_color_cell = self.game.get_cell(new_head).color
        if next_color_cell == consts.back_color:
            temp = self.cells.pop(0)
            self.game.get_cell(temp).set_color(consts.back_color)
            self.cells.append(new_head)
            self.game.get_cell(new_head).set_color(self.color)
        elif next_color_cell == consts.fruit_color:
            self.cells.append(new_head)
            self.game.get_cell(new_head).set_color(self.color)
        else:
            self.game.kill(self)

    def handle(self, keys):
        for key in keys:
            if key in self.keys and self._check_direction(self.keys[key]):
                self.direction = self.keys[key]
                break

    def _check_direction(self, key_dir):
        temp = [key_dir, self.direction]
        if "UP" in temp and "DOWN" in temp:
            return False
        if "LEFT" in temp and "RIGHT" in temp:
            return False
        return True
