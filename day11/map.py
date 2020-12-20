with open("input.txt") as r:
    grid_layout = r.readlines()


# parse
width = len(grid_layout[0].strip())
height = len(grid_layout)
def parse(grid_layout):
    new_grid = []
    for i in range(height):
        new_grid.append([g for g in grid_layout[i] if g != "\n"])
    return new_grid
grid_layout= parse(grid_layout)

import copy
original_grid = copy.deepcopy(grid_layout)

def get_adj_count(adjacents):
    adj_occ_count = 0
    for a in adjacents:
        if a == "#":
            adj_occ_count+=1
    return adj_occ_count, len(adjacents) -adj_occ_count

def cell_decision(grid, seat_id, no_count):
    global original_grid
    i,j = seat_id
    adjacents = []
    for coor in [[1,1], [-1,-1], [1,-1], [-1,1], [0,1], [1,0], [0,-1], [-1,0]]:
        i_c,j_c = coor
        i_c += i
        j_c += j
        if (i_c>=0 and i_c<height) and (j_c>=0 and j_c<width):
            adjacents.append(original_grid[i_c][j_c])

    adj_occ, adj_not_occ = get_adj_count(adjacents)
    if original_grid[i][j] == "L" and adj_not_occ == len(adjacents):
        grid[i][j] = "#"
    elif original_grid[i][j]  == "#" and adj_occ >= 4:
        grid[i][j]= "L"
    else:
        no_count += 1
        pass
    return grid, no_count


def visualize(grid_layout):
    gw = []
    for gr in grid_layout:
        gw.append("".join(gr))
        gw += ["\n"]
    gw = "".join(gw)
    print(gw)
def change_grid(grid_layout):
    no_count = 0
    for i in range(height):
        for j in range(width):
            grid_layout, no_count = cell_decision(grid_layout, (i,j), no_count)
    return grid_layout ,no_count == (width*height)
def simulate(grid_layout):
    while True:
        grid_layout, stable = change_grid(grid_layout)
        original_grid = copy.deepcopy(grid_layout)
        if stable:
            break
    occ_count = 0
    for grid_row in grid_layout:
        occ_count += grid_row.count("#")
    print(occ_count)


#---------------------------------------part2------------------------------------------------

with open("input.txt") as r:
    grid_layout = r.readlines()


def visualize(grid_layout):
    gw = []
    for gr in grid_layout:
        gw.append("".join(gr))
        gw += ["\n"]
    gw = "".join(gw)
    print(gw)
# parse
width = len(grid_layout[0].strip())
height = len(grid_layout)

def parse(grid_layout):
    new_grid = []
    for i in range(height):
        new_grid.append([g for g in grid_layout[i] if g != "\n"])
    return new_grid
grid_layout= parse(grid_layout)
import copy
original_grid = copy.deepcopy(grid_layout)

def get_adj_count(adjacents):
    adj_occ_count = 0
    for a in adjacents:
        if a == "#":
            adj_occ_count+=1
    return adj_occ_count, len(adjacents) -adj_occ_count
def cell_decision2(grid, seat_id, no_count):
    global original_grid
    i,j = seat_id
    adjacents = []
    for coor in [[1,1], [-1,-1], [1,-1], [-1,1], [0,1], [1,0], [0,-1], [-1,0]]:
        i_c,j_c = coor
        move_y, move_x = i_c, j_c

        i_c += i
        j_c += j
        while True:
            if (i_c>=0 and i_c<height) and (j_c>=0 and j_c<width):
                if original_grid[i_c][j_c] != '.':
                    adjacents.append(original_grid[i_c][j_c])
                    break
            else:
                break

            i_c+=move_y
            j_c+=move_x

    adj_occ, adj_not_occ = get_adj_count(adjacents)
    if original_grid[i][j] == "L" and adj_not_occ == len(adjacents):
        grid[i][j] = "#"
    elif original_grid[i][j]  == "#" and adj_occ >= 5:
        grid[i][j]= "L"
    else:
        no_count += 1
        pass
    return grid, no_count


def change_grid2(grid_layout):
    no_count = 0
    for i in range(height):
        for j in range(width):
            grid_layout, no_count = cell_decision2(grid_layout, (i,j), no_count)
    return grid_layout ,no_count == (width*height)

def simulate2(grid_layout):
    global original_grid
    while True:
        grid_layout, stable = change_grid2(grid_layout)
        original_grid = copy.deepcopy(grid_layout)
        if stable:
            break
    occ_count = 0
    for grid_row in grid_layout:
        occ_count += grid_row.count("#")
    print(occ_count)
simulate2(grid_layout)
