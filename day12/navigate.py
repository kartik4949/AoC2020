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

def rotate90(x,direction, i,c=True):
    new_x = (direction + i)%4 if c else direction - i
    new_x = new_x if new_x >=0 else 4 + new_x
    WAYPOINT[new_x] = x
    WAYPOINT[direction]=0

def waypoint_rot(rotidx):
    x = max(WAYPOINT[0],WAYPOINT[2])
    ix = WAYPOINT.index(x)
    y = max(WAYPOINT[1],WAYPOINT[3])
    iy = WAYPOINT.index(y)
    c = True if rotidx>0 else False
    rotate90(x, ix,rotidx,c)
    rotate90(y,iy,rotidx,c)


class Ship:
    direction = 0
    man_distance = 0




def move_waypoint(move, d):
    global WAYPOINT
    opp_move =  WAYPOINT[(d +2)%4]
    if ship.direction == d and opp_move ==0:
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
def action(ship, d, move):
    global DIRECTION
    if d == "F":
        movey = max(WAYPOINT[1],WAYPOINT[3])
        ixd = WAYPOINT.index(movey)
        movex = max(WAYPOINT[0],WAYPOINT[2])
        iyd = WAYPOINT.index(movex)
        move_ship(ship, movey, iyd)
        move_ship(ship, movex, ixd)
    elif d == "R" or d=="L":
        i = move // 90
        waypoint_rot(i)
    else:
        move_ship(waypoint, move,DIRECTION.index(d))

def decode_direction(d):
    return d[0], int(d[1:])

ship = Ship()
waypoint = Waypoint()
for d in directions:
   direction, move = decode_direction(d)
   action(ship, waypoint, direction, move)
print(sum(MOVE))
