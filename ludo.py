######################### مهرداد اسلام ##########################
#Project_Ludo

import random

ranking = []

R = [-1, -1, -1, -1]

B = [-1, -1, -1, -1]

G = [-1, -1, -1, -1]

Y = [-1, -1, -1, -1]


def dice():
    return random.randint(1,6)

def cycle(value):
    range_size = 40
    wrapped_value = (value - 1) % range_size + 1
    return wrapped_value

def roll():
    inp = input("Write roll to roll the dice: ")
    if inp == "roll":
        global rolled
        rolled = dice()
        print(f"You rolled {rolled}")
        return rolled
    else:
        print("Roll in right way!cheater!")
        roll()

def check_list(lst):
    count_44 = lst.count(44) 
    negatives = all(x < 0 for x in lst if x != 44) 

    if (count_44 == 1 and negatives) or (count_44 == 2 and negatives) or (count_44 == 3 and negatives):
        return True
    return False

def choice(p, roll):
    if roll != 6 and (all(piece < 0 for piece in p) or (check_list(p))):
        print("You can't move any of your pieces")
        return None
    else:
        print("Which piece would you like to move?")
        for i in range(4):
            print(f"{i+1}. mohre {i+1}")
        inp = input("choose a piece: ")
        global esm
        esm = inp
        if inp in ["1", "2", "3", "4"]:
            piece = int(inp) - 1
            print(p[piece])
            if piece is None:
                print("Invalid piece, try again")
                return choice(p)
            elif piece < 0 and roll == 6:
                return piece
            elif piece < 0:
                print("You can't move this piece, try another")
                return choice(p)
            elif piece >= 44:
                print("This piece has already won, try another")
                return choice(p)
            elif piece < 44:
                return piece

def move(mohre, roll_value, c):
    if roll_value == 6:
        if c[mohre] < 0:
            c[int(mohre)] = 1
            print(f"You've entered the game with {mohre + 1} and you've got another chance")
            print(c)
            new_roll = roll()
            mohre = choice(c, new_roll)
            move(mohre, new_roll, c)
        else:
            c[mohre] += roll_value
            print("You've got another chance")
            new_roll = roll()
            print(new_roll)
            mohre = choice(c, new_roll)
            move(mohre, new_roll, c)
    else:
        if c[mohre] < 0:
            print("You can't move, choose another piece")
            choice(c, roll_value)
            return mohre
        else:
            c[mohre] += roll_value
            print(f"Moved to {c[mohre]}")
            return mohre
        
def check_r(r):
    for i in range(4):
        if cycle(r - 10) == B[i]:
            B[i] = -1
            print(f"B{i+1} is out")

    for i in range(4):
        if cycle(r - 20) == G[i]:
            G[i] = -1
            print(f"G{i+1} is out")

    for i in range(4):
        if cycle(r + 10) == Y[i]:
            Y[i] = -1
            print(f"Y{i+1} is out")

def check_b(r):
    for i in range(4):
        if cycle(r + 10) == R[i]:
            B[i] = -1
            print(f"B{i+1} is out")

    for i in range(4):
        if cycle(r - 10) == G[i]:
            G[i] = -1
            print(f"G{i+1} is out")

    for i in range(4):
        if cycle(r - 20) == Y[i]:
            Y[i] = -1
            print(f"Y{i+1} is out")

def check_g(r):
    for i in range(4):
        if cycle(r + 20) == R[i]:
            G[i] = -1
            print(f"G{i+1} is out")

    for i in range(4):
        if cycle(r + 10) == B[i]:
            B[i] = -1
            print(f"B{i+1} is out")

    for i in range(4):
        if cycle(r - 10) == Y[i]:
            Y[i] = -1
            print(f"Y{i+1} is out")

def check_y(r):
    for i in range(4):
        if cycle(r - 10) == R[i]:
            Y[i] = -1
            print(f"Y{i+1} is out")

    for i in range(4):
        if cycle(r - 20) == B[i]:
            B[i] = -1
            print(f"B{i+1} is out")

    for i in range(4):
        if cycle(r + 10) == G[i]:
            G[i] = -1
            print(f"G{i+1} is out")

m = [[ 0, 0, 0, 0,39,40, 1, 0, 0, 0, 0],
     [ 0, 0, 0, 0,38,41, 2, 0, 0, 0, 0],
     [ 0, 0, 0, 0,37,42, 3, 0, 0, 0, 0],
     [ 0, 0, 0, 0,36,43, 4, 0, 0, 0, 0],
     [31,32,33,34,35,44, 5, 6, 7, 8, 9],
     [30,55,56,57,58, 0,48,47,46,45,10],
     [29,28,27,26,25,54,15,14,13,12,11],
     [ 0, 0, 0, 0,24,53,16, 0, 0, 0, 0],
     [ 0, 0, 0, 0,23,52,17, 0, 0, 0, 0],
     [ 0, 0, 0, 0,22,51,18, 0, 0, 0, 0],
     [ 0, 0, 0, 0,21,20,19, 0, 0, 0, 0]]

a = [['  ', '  ', '  ', '  ', '00', '00', '00', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '00', '  ', '00', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '00', '  ', '00', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '00', '  ', '00', '  ', '  ', '  ', '  '],
     ['00', '00', '00', '00', '00', '  ', '00', '00', '00', '00', '00'],
     ['00', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '00'],
     ['00', '00', '00', '00', '00', '  ', '00', '00', '00', '00', '00'],
     ['  ', '  ', '  ', '  ', '00', '  ', '00', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '00', '  ', '00', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '00', '  ', '00', '  ', '  ', '  ', '  '],
     ['  ', '  ', '  ', '  ', '00', '00', '00', '  ', '  ', '  ', '  ']]

def show_r(x):
    for i in range(11):
        for j in range(11):
            if a[i][j] == f"R{esm}":
                a[i][j] = "00"
            if x == m[i][j]:
                for k in range(4):
                    if x == R[k]:
                        print(R[k])
                        a[i][j] = f"R{k + 1}"
    for t in a:
        print(t)

def show_b(x):
    for i in range(11):
        for j in range(11):
            if a[i][j] == f"B{esm}":
                a[i][j] = "00"

            if x > 40:
                b1 = x + 4
                if b1 == m[i][j]:
                    for k in range(4):
                        a[i][j] = f"B{k + 1}"

            elif cycle(x + 10) == m[i][j]:
                for k in range(4):
                    if x == B[k]:
                        a[i][j] = f"B{k + 1}"
            

    for t in a:
        print(t)
                
def show_g(x):
    for i in range(11):
        for j in range(11):
            if a[i][j] == f"G{esm}":
                a[i][j] = "00"
            
            if x > 40:
                b1 = x + 10
                if b1 == m[i][j]:
                    for k in range(4):
                        a[i][j] = f"G{k + 1}"
            
            elif cycle(x + 20) == m[i][j]:
                for k in range(4):
                    if x == G[k]:
                        a[i][j] = f"G{k + 1}"
            
    for t in a:
        print(t)

def show_y(x):
    for i in range(11):
        for j in range(11):
            if a[i][j] == f"Y{esm}":
                a[i][j] = "00"

            if x > 40:
                b1 = x + 14
                if b1 == m[i][j]:
                    for k in range(4):
                        a[i][j] = f"Y{k + 1}"

            elif cycle(x + 30) == m[i][j]:
                for k in range(4):
                    if x is Y[k]:
                        a[i][j] = f"Y{k + 1}"
           
    for t in a:
        print(t)

def check_win(mohre, player_name):
    if all(piece >= 44 for piece in mohre) and player_name not in ranking:
        ranking.append(player_name)
        print(f"{player_name} has finished the game! Current rank: {len(ranking)}")
        return True
    return False

while len(ranking) < 4:
    print("########## Red's turn ############")
    rolled = roll()
    mohre = choice(R, rolled)
    if mohre is not None:
        move(mohre, rolled, R)
        check_r(R[mohre])
        show_r(R[mohre])
        if check_win(R, "Red"):
            continue

    print("############# Blue's turn ###########")
    rolled = roll()
    mohre = choice(B, rolled)
    if mohre is not None:
        move(mohre, rolled, B)
        check_b(B[mohre])
        show_b(B[mohre])
        if check_win(B, "Blue"):
            continue
    
    print("############## Green's turn ############")
    rolled = roll()
    mohre = choice(G, rolled)
    if mohre is not None:
        move(mohre, rolled, G)
        check_g(G[mohre])
        show_g(G[mohre])
        if check_win(G, "Green"):
            continue

    print("############### Yellow's turn ############")
    rolled = roll()
    mohre = choice(Y, rolled)
    if mohre is not None:
        move(mohre, rolled, Y)
        check_y(Y[mohre])
        show_y(Y[mohre])
        if check_win(Y, "Yellow"):
            continue

print("Game over! Ranking:")
for i, player in enumerate(ranking):
    print(f"{i+1}. {player}")

