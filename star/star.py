import random

<<<<<<< HEAD
# Define the ASCII characters for the stars- hamid
=======
# Define the ASCII characters for the stars
>>>>>>> cd47b9f1ba4889a61c75bb40e4c418e1021887cc
star_chars = ['\u2665', '\u2605', '\u2600', '@', '0', 'Q', '.']

# function to define random 2D list that 3 number in row and col are not the same.
def generate_random_2d_list():
    global row_num, col_num
    rand_list = []
    for i in range(row_num):
        row = []
        while len(row) < col_num:
            num = random.randint(0, 4)
            if len(row) < 2 or num != row[-1] or num != row[-2]:
                valid_col = False
                if len(rand_list) < 2 or rand_list[len(rand_list) - 1][len(row)] != num:
                    valid_col = True
                    if valid_col:
                        row.append(num)
        rand_list.append(row)
    return rand_list

# function to print board game. "define a random_list for this function."
def board_game():
    global row_num, col_num
    global rand_list
    print(f'\nmove left: {move_left}')
    print(f'score: {score}\n')
    for i in range(row_num):
        for j in range(col_num):
            if i == cursor_y and j == cursor_x:
                print(chr(0x1F6F8), end='  ')
            else:    
                print(star_chars[rand_list[i][j]], end='   ')
        print('\n')
        
# function to move cursor location by user input
def move_cursor():
    global cursor_x, cursor_y
    global row_num, col_num

    print('-' * 50)
    key = input('''
-Move ship : 'W', 'S', 'A', 'D'
-swap : 'G'
-Bomb : 'B'
-Menu : 'Q'\n
-your choice: ''').lower()

    for i in key:
        if i == 'w':
            cursor_y -= 1
        elif i == 's':
            cursor_y += 1
        elif i == 'd':
            cursor_x += 1
        elif i == 'a':
            cursor_x -= 1
        elif i == 'g' or i == 'q':
            return i
        elif i == 'b' and rand_list[cursor_y][cursor_x] == 5:
            bomb()
            return i
        if cursor_x >= col_num:
            cursor_x = 0
        elif cursor_x < 0:
            cursor_x = col_num + cursor_x
        if cursor_y >= row_num:
            cursor_y = 0
        elif cursor_y < 0:
            cursor_y = row_num + cursor_y


# function that swaps cells
def swap_cell():
    global cursor_x, cursor_y
    global row_num, col_num
    key = input("Which way do you want to move? ('W', 'S', 'A', 'D')").lower()
    print('-' * 50)
    temp = rand_list[cursor_y][cursor_x]
    if key == 'w' and cursor_y > 0:
        rand_list[cursor_y][cursor_x] = rand_list[cursor_y - 1][cursor_x]
        rand_list[cursor_y - 1][cursor_x] = temp
    elif key == 's' and cursor_y < row_num:
        rand_list[cursor_y][cursor_x] = rand_list[cursor_y + 1][cursor_x]
        rand_list[cursor_y + 1][cursor_x] = temp
    elif key == 'a' and cursor_x > 0:
        rand_list[cursor_y][cursor_x] = rand_list[cursor_y][cursor_x - 1]
        rand_list[cursor_y][cursor_x - 1] = temp
    elif key == 'd' and cursor_y < col_num:
        rand_list[cursor_y][cursor_x] = rand_list[cursor_y][cursor_x + 1]
        rand_list[cursor_y][cursor_x + 1] = temp


# function to print menu bar and return choice of user
def menu():
    print('\n\t--STAR GAME--\n\n1. START\n2. How to play?\n3. About me\n4. Exit\n')
    choice = input('Enter your choice. (1, 2, 3 or 4):  ')
    return choice


# Define a function to check for match
def check_matches():
    global rand_list
    global score
    global row_num, col_num
    global cursor_x, cursor_y

    # Check for horizontal repetitions
    repeated_row = []
    for i in range(row_num):
        count = 1
        for j in range(col_num - 1):
            if rand_list[i][j] == rand_list[i][j + 1]:
                count += 1
            else:
                if count >= 3:
                    repeated_row.append((rand_list[i][j], count, i, j))
                count = 1
        if count >= 3:
            repeated_row.append((rand_list[i][-1], count, i, col_num - 1))

    # Check for vertical repetitions
    repeated_col = []
    rotate_rand_list = list(zip(*rand_list))
    for j in range(col_num):
        count = 1
        for i in range(row_num - 1):
            if rotate_rand_list[j][i] == rotate_rand_list[j][i + 1]:
                count += 1
            else:
                if count >= 3:
                    repeated_col.append((rotate_rand_list[j][i], count, i, j))
                count = 1
        if count >= 3:
            repeated_col.append((rotate_rand_list[j][-1], count, row_num - 1, j))

    # horizontal: score, replace similar element with -1 and bomb for 4 similar element
    for element, count, i, j in repeated_row:
        score += count * 10
        for k in range(count, 0, -1):
            rand_list[i][j - k + 1] = -1
        if count >= 4:
            rand_list[cursor_y][cursor_x] = 5

    # vertical: score, replace similar element with -1 and bomb for 4 similar element
    for element, count, i, j in repeated_col:
        score += count * 10
        for k in range(count, 0, -1):
            rand_list[i - k + 1][j] = -1
        if count >= 4:
            rand_list[random.randint(0, row_num-1)][random.randint(0, col_num-1)] = 5


# Define a Function to blow up a row and column
def bomb():
    global row_num, col_num
    global cursor_x, cursor_y

    for i in range(row_num):
        rand_list[i][cursor_x] = -1
    for j in range(col_num):
        rand_list[cursor_y][j] = -1


# Function that while -1 in rand list:
# print board and replaces exploded stars with top stars and check matches again..
def replace_star():
    global row_num, col_num
    global rand_list
    while any(-1 in row for row in rand_list):
        board_game()
        for j in range(col_num):
            if rand_list[0][j] == -1:
                rand_list[0][j] = random.randint(0, 4)

        for i in range(1, row_num):
            for j in range(col_num):
                if rand_list[i][j] == -1:
                    for k in range(i):
                        rand_list[i - k][j] = rand_list[i - k - 1][j]
                    rand_list[0][j] = random.randint(0, 4)
        check_matches()

# Define a game loop 
while True:

    # Define the user's score
    score = 0

    # Define move left
    move_left = 10

    # Define the cursor position
    cursor_x, cursor_y = 0, 0

    # Define the number of row and column
    row_num, col_num = 6, 8

    menu_num = menu()
    if menu_num == '1':
        rand_list = generate_random_2d_list()

        # The user can stay in the game until his chances are over
        while move_left > 0:
            board_game()
            var = move_cursor()
            while var != 'g' and var != 'q' and var != 'b':
                board_game()
                var = move_cursor()
            while var == 'b':
                replace_star()
                board_game()
                var = move_cursor()
                while var != 'g' and var != 'q' and var != 'b':
                    board_game()
                    var = move_cursor()
            if var == 'q':
                break

            swap_cell()
            move_left -= 1
            check_matches()
            replace_star()

        print(f'\n---END GAME---\nYour Score: {score}\nGood Luck.\n')

    # How to play?
    elif menu_num == '2':
        massage = '''
        \nMove:
        move on the cursor on board
        game with 'W', 'S', 'A', 'D'.
        for example:'aaw' means 2 moves
        to left and 1 move to top.
        \nSelect:
        select shape with 'G' and swipe
        it with surrounding cells
        with 'W', 'S', 'A', 'D' and
        match 3 cells of the same shape
        and clear them.
        \nScore:
        if you match 3 cell
        you get 30 point.
        4 cells match = 40 point
        and so on.:)
        \nGift:
        if you match 4 items, you give a
        bomb ('Q') and by selecting ('B'),
        one row and column is blow up.
        booom!!
        '''
        print(massage)

    # About me
    elif menu_num == '3':
       print('\n\t\t---About me---\nIm FARHAD.\nEmail: nakhaie.farhad@gamil.com')

    # Exit
    elif menu_num == '4':
        print('\nBye.')
        break
