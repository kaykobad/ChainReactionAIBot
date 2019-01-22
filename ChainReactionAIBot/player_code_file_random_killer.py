import time
import random
import sys
import copy

grid_size = 8
global grid, player_color, move_count


def valid(x, y):
    if 0<=x<grid_size and 0<=y<grid_size:
        return True
    return False


def get_extra_weight(x, y):
    if x in [0, 7] and y in [0, 7]:
        # corner
        return 2
    elif x in [0, 7] and y in [1, 2, 3, 4, 5, 6]:
        # edge
        return 1
    elif y in [0, 7] and x in [1, 2, 3, 4, 5, 6]:
        # edge
        return 1
    else:
        return 0


def get_enemy_count(x, y):
    count = 0;
    global player_color, grid
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(len(dx)):
        p = dx[i]
        q = dy[i]
        new_x = x+p
        new_y = y+q

        if valid(new_x, new_y) and grid[new_x][new_y] != 'No' and grid[new_x][new_y][0] != player_color:
            count += int(grid[new_x][new_y][1])

    return count+int(grid[x][y][1])+get_extra_weight(x, y)


def read_file(player_color):
    # global grid
    with open("shared_file.txt") as f:
        lines = f.readlines()
    if len(lines) == 0:
        return None
    if lines[0].strip('\n') == str(player_color):
        temp_grid = []
        for line in lines[1:]:
            temp_grid.append(line.strip('\n').split(" ")[:-1])

        # grid = copy.deepcopy(temp_grid)
        return temp_grid
    return None


def select_move(grid, player_color):
    global move_count
    own = []
    enemy = []
    dis = -1
    xx = -1
    yy = -1
    if move_count < 20:
        val = 500
        x = -1
        y = -1
        for i in range (grid_size):
            for j in range(grid_size):
                if grid[i][j] == 'No' and i+j < val:
                    val = i+j
                    x = i
                    y = j
        move_count += 1
        return x, y

    for i in range(grid_size):
        for j in range(grid_size):
            if (grid[i][j][0] == player_color):
                own.append((i, j))

    for pos1 in own:
        cnt = get_enemy_count(pos1[0], pos1[1])

        if cnt > dis:
            dis = cnt
            xx = pos1[0]
            yy = pos1[1]

    # print(xx, yy)
    return xx, yy
    """
    else:
        for i in range (grid_size):
            for j in range(grid_size):
                if(grid[i][j][0] == player_color):
                    own.append((i, j))
                elif grid[i][j][0] != 'N':
                    enemy.append((i, j))
    for pos1 in own:
        for pos2 in enemy:
            if(abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])< dis):
                dis = abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])
                xx = pos1[0]
                yy = pos1[1]
                #print(dis)

    print(xx, yy)
    return  xx, yy
    """

def write_move(move):
    str_to_write = '0\n' + str(move[0]) + " " + str(move[1])
    with open("shared_file.txt", 'w') as f:
        f.write(str_to_write)


def main():
    global grid_size, grid, player_color, move_count
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