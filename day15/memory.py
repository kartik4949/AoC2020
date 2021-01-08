import collections
turns = [7,12,1,0,16,2]
hashtable = collections.defaultdict(list)
hashtable.update({7:[0], 12:[1], 1:[2], 0:[3], 16:[4], 2:[5]})

i =len(turns)
def check_latest_match(turns, number):
    for i, prev in enumerate(reversed(turns[:-1])):
        if prev==number:
            return prev, len(turns[:-1]) - i
    return None
last_s_n = turns[-1]
while True:
    prev_value = hashtable[last_s_n]
    in_prev = prev_value if len(prev_value) else False
    if in_prev:
        if len(in_prev) > 1:
            idx = in_prev[-2]
        else:
            idx = in_prev[-1]
        new_num = (i-1) - idx
        last_s_n = new_num
        new_num_list = hashtable[new_num]
        new_num_list.append(i)
        hashtable[new_num] = new_num_list
    else:
        if i == len(turns):
            hashtable[turns[-1]].append(2)
        hashtable[0].append(i)
        last_s_n = 0
    i+=1
    if i==30000000:
        print(last_s_n)
        break

