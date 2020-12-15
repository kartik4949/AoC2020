with open('input.txt') as r:
    boarding_passes = r.readlines()



def get_coor(boarding_pass, row_range):
    seats = row_range
    for row in boarding_pass:
        half_way = int((seats[1] - seats[0] )/2 -.5) + seats[0]
        if row in ("F", "L") :
            seats[1] = half_way
        elif row in ("B", "R"):
            seats[0] = half_way + 1
    return seats[1]
def get_seat(boarding_pass):
    boarding_pass = boarding_pass.strip()
    return get_coor(boarding_pass[:7], row_range=[0,127])*8 + get_coor(boarding_pass[-3:], row_range=[0,7])
print(max(map(get_seat, boarding_passes)))

def get_row_column(boarding_pass):
    boarding_pass = boarding_pass.strip()
    return get_coor(boarding_pass[:7], row_range=[0,127]),  get_coor(boarding_pass[-3:], row_range=[0,7])

seatids = []
for boarding_pass in boarding_passes:
    row, column  = get_row_column(boarding_pass)
    if row >0 and row < 127:
        seatids.append((row, column))

import itertools
all_seats = list(itertools.product(range(1,127), range(0,8)))
missing_seats = list(set(all_seats).difference(seatids))
missing_seats = list(map(lambda x: x[0]*8 + x[1], missing_seats))
def get_your_seat(missing_seats):
    for i in range(0, len(missing_seats)):
        if not ((missing_seats[i]+1) in missing_seats and (missing_seats[i]+1) in missing_seats):
            return missing_seats[i]
your_seat = get_your_seat(missing_seats)
print(your_seat)
