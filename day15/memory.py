turns = [7,12,1,0,16,2]

i =len(turns) + 1
def check_latest_match(turns, number):
    for i, prev in enumerate(reversed(turns[:-1])):
        if prev==number:
            return prev, len(turns[:-1]) - i
    return None
while True:
    last_s_n = turns[-1]
    in_prev= check_latest_match(turns, last_s_n)
    if in_prev:
        prev_num, idx = in_prev
        turns.append((i-1) - idx)
    else:
        turns.append(0)
    i+=1
    if i==30000001:
        print(turns[-1])
        break

