with open("input.txt") as r:
    XAMS = r.readlines()

preamble_size = 25
import itertools
def check_preamble(preamble, numbers=2):
    number = preamble[-1].strip()
    preamble = preamble[:-1]
    flag = False
    for i,j in itertools.combinations(preamble, numbers):
        i, j = i.strip(), j.strip()
        if (int(i) + int(j)) == int(number):
            flag = True
            break
    return flag, number
ps = 0
pe = preamble_size +1
while True:
    flag, n = check_preamble(XAMS[ps:pe])
    if not flag:
        print(n)
        break
    ps, pe = ps+1, pe + 1

XAMS_breakage = n
def check_atleast(preamble, numbers=2, breakage_number=0):
    flag = False
    number = 0
    for s in range(len(preamble) - numbers):
        comb_numbers = preamble[s:s+numbers]
        if sum([int(n.strip()) for n in comb_numbers]) == int(breakage_number):
            flag = True
            number=comb_numbers
            break
    return flag, number
#---------------------------------part2------------------------------------------------
numbers = 2
while True:
    flag, list_number = check_atleast(XAMS, numbers=numbers, breakage_number=XAMS_breakage)
    if flag:
        list_number = sorted(list_number)
        print(int(list_number[0].strip()) + int(list_number[-1].strip()))
        break
    numbers += 1


