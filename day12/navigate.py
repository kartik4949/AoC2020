with open("input.txt") as r:
    directions = r.readlines()

DIRECTION = ["E", "S", "W", "N"]
MOVE = [0,0,0,0]


class Ship:
    direction = 0
    man_distance = 0
def move_ship(ship, move, d):
    global MOVE
    opp_move =  MOVE[(d +2)%4]
    if ship.direction == d and opp_move ==0:
        MOVE[d] += move
    else:
        if move > opp_move:
            MOVE[d] +=  int(move - opp_move)
            MOVE[(d +2)%4] = 0

        elif move <= opp_move:
            MOVE[(d +2)%4] = int(opp_move - move)
def action(ship, d, move):
    global DIRECTION
    if d == "F":
        move_ship(ship, move, ship.direction)
    elif d == "R" or d=="L":
        i = move // 90
        ship.direction = (ship.direction + i)%4 if d == "R" else ship.direction - i
        ship.direction = ship.direction if ship.direction >=0 else 4 +ship.direction
    else:
        move_ship(ship, move,DIRECTION.index(d))

def decode_direction(d):
    return d[0], int(d[1:])

ship = Ship()

for d in directions:
   direction, move = decode_direction(d)
   action(ship, direction, move)
print(sum(MOVE))



# ------------------------------part2------------------------------------

with open("input.txt") as r:
    directions = r.readlines()

DIRECTION = ["E", "S", "W", "N"]
MOVE = [0,0,0,0]
WAYPOINT = [10,0,0,1]

def rotate90(x,direction, i,c):
    global WAYPOINT
    new_x = (direction + i)%4 if c else direction - i
    new_x = new_x if new_x >=0 else 4 + new_x
    WAYPOINT[direction]=0
    return new_x, x
    #WAYPOINT[new_x] = x

def waypoint_rot(rotidx,c):
    global WAYPOINT
    iyd = np.argmax(np.asarray(WAYPOINT)[[1,3]])
    iy = 1 if iyd == 0 else 3
    y = WAYPOINT[iy]
    ixd = np.argmax(np.asarray(WAYPOINT)[[0,2]])
    ix = 0 if ixd == 0 else 2
    x = WAYPOINT[ix]
    new_x_idx,xv = rotate90(x, ix,rotidx,c)
    new_y_idx, yv =rotate90(y,iy,rotidx,c)
    WAYPOINT[new_x_idx] = xv
    WAYPOINT[new_y_idx] = yv


class Ship:
    direction = 0
    man_distance = 0




def move_waypoint(move, d):
    global WAYPOINT
    opp_move =  WAYPOINT[(d +2)%4]
    if WAYPOINT[d] > 0 and opp_move ==0:
        WAYPOINT[d] += move
    else:
        if move > opp_move:
            WAYPOINT[d] +=  int(move - opp_move)
            WAYPOINT[(d +2)%4] = 0

        elif move <= opp_move:
            WAYPOINT[(d +2)%4] = int(opp_move - move)

def move_ship(ship, move, d):
    global MOVE
    opp_move =  MOVE[(d +2)%4]
    if ship.direction == d and opp_move ==0:
        MOVE[d] += move
    else:
        if move > opp_move:
            MOVE[d] +=  int(move - opp_move)
            MOVE[(d +2)%4] = 0

        elif move <= opp_move:
            MOVE[(d +2)%4] = int(opp_move - move)
import numpy as np
def action(ship, d, move):
    global DIRECTION
    global WAYPOINT
    if d == "F":
        iyd = np.argmax(np.asarray(WAYPOINT)[[1,3]])
        iyd = 1 if iyd == 0 else 3
        movey = WAYPOINT[iyd]
        ixd = np.argmax(np.asarray(WAYPOINT)[[0,2]])
        ixd = 0 if ixd == 0 else 2
        movex = WAYPOINT[ixd]
        move_ship(ship, movey*move, iyd)
        move_ship(ship, movex*move, ixd)
    elif d == "R" or d=="L":
        i = move // 90
        waypoint_rot(i,True if d =="R" else False)
    else:
        move_waypoint( move,DIRECTION.index(d))

def decode_direction(d):
    return d[0], int(d[1:])

ship = Ship()
for d in directions:
   direction, move = decode_direction(d)
   action(ship,direction, move)
print(sum(MOVE))
