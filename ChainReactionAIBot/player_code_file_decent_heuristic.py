import time
import random
import sys
import copy
import time


grid_size = 8

global grid, player_color, move_count


def read_file(player_color):
    with open("shared_file.txt") as f:
        lines = f.readlines()
    if len(lines) == 0:
        return None
    if lines[0].strip('\n') == str(player_color):
        temp_grid = []
        for line in lines[1:]:
            temp_grid.append(line.strip('\n').split(" ")[:-1])

        return temp_grid
    return None

#


def chains(gd):
    board = copy.deepcopy(gd)
    lengths = []
    for pos in [(x,y) for x in range(grid_size) for y in range(grid_size)]:
        if board[pos[0]][pos[1]] != 'No' and (int(board[pos[0]][pos[1]][1]) == (critical_mass(pos) - 1) and board[pos[0]][pos[1]][0] == player_color):
            l = 0
            visiting_stack = []
            visiting_stack.append(pos)
            while visiting_stack:
                pos = visiting_stack.pop()
                board[pos[0]][pos[1]] = 'No'
                l += 1
                for i in neighbors(pos):
                    if board[pos[0]][pos[1]] != 'No' and (int(board[pos[0]][pos[1]][1]) == (critical_mass(i) - 1) and board[pos[0]][pos[1]][0] == player_color):
                        visiting_stack.append(i)
            lengths.append(l)
    return lengths


def critical_mass(pos):
    if pos == (0, 0) or pos == (grid_size - 1, grid_size - 1) or pos == (grid_size - 1, 0) or pos == (0, grid_size - 1):
        return 2
    elif pos[0] == 0 or pos[0] == grid_size-1 or pos[1] == 0 or pos[1] == grid_size-1:
        return 3
    else:
        return 4


def neighbors(pos):
    n = []
    for i in [(pos[0],pos[1]+1), (pos[0],pos[1]-1), (pos[0]+1,pos[1]), (pos[0]-1,pos[1])]:
        if 0 <= i[0] < grid_size and 0 <= i[1] < grid_size:
            n.append(i)
    return n


def score(pos, grd):
    grid = copy.deepcopy(grd)
    sc = 0
    my_orbs, enemy_orbs = 0, 0
    if(grid[pos[0]][pos[1]][0] != player_color or (grid[pos[0]][pos[1]][0] == player_color and grid[pos[0]][pos[1]][1] == critical_mass(pos))):
        return -10000
    for ps in [(x, y) for x in range(grid_size) for y in range(grid_size)]:
        if grid[ps[0]][ps[1]][0] == player_color:
            my_orbs += int(grid[ps[0]][ps[1]][1])
            flag_not_vulnerable = True
            for i in neighbors(pos):
                if grid[ps[0]][ps[1]][0] != player_color and (int(grid[ps[0]][ps[1]][1]) == critical_mass(i) - 1):
                    sc -= 5-critical_mass(pos)
                    flag_not_vulnerable = False
            if flag_not_vulnerable:
                #The edge Heuristic
                if critical_mass(pos) == 3:
                    sc += 2
                #The corner Heuristic
                elif critical_mass(pos) == 2:
                    sc += 3
                #The unstability Heuristic
                if grid[ps[0]][ps[1]][0] == player_color and int(grid[ps[0]][ps[1]][1]) == critical_mass(pos) - 1:
                    sc += 2
                #The vulnerablity Heuristic
        elif grid[ps[0]][ps[1]] != 'No':
            enemy_orbs += int(grid[ps[0]][ps[1]][1])
    #The number of Orbs Heuristic
    sc += my_orbs
    #You win when the enemy has no orbs
    if enemy_orbs == 0 and my_orbs > 1:
        return 10000
    #You loose when you have no orbs
    elif my_orbs == 0 and enemy_orbs > 1:
        return -10000
    #The chain Heuristic
    sc += sum([2*i for i in chains(grid) if i > 1])
    return sc

#

def select_move(grid, player_color):
    global move_count

    if move_count < 20:
        while True:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if grid[x][y] == 'No':
                move_count += 1
                # print(x, y, move_count)
                return x, y

    best_score = -9999999
    for pos in [(x, y) for x in range(grid_size) for y in range(grid_size)]:
        val = score(pos, grid)
        if val>best_score:
            best_score = val
            best_move = pos

    # print(best_move[0], best_move[1])
    move_count += 1
    return best_move[0], best_move[1]
    '''
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if grid[x][y] == 'No' or grid[x][y][0] == player_color:
            return x, y
    '''


def write_move(move):
    str_to_write = '0\n' + str(move[0]) + " " + str(move[1])
    with open("shared_file.txt", 'w') as f:
        f.write(str_to_write)


def main():
    global player_color, grid, move_count
    move_count = 0
    player_color = sys.argv[1]
    while True:
        while True:
            # grid = read_file(player_color)
            grid = read_file(player_color)
            if grid is not None:
                break
            time.sleep(.01)
        move = select_move(grid, player_color)
        write_move(move)


if __name__ == "__main__":
    main()
