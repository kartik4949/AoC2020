with open("input.txt") as r:
    adapters = r.readlines()


starting_jolt = 0

def find_adapter(current_jolt, adapters,jolt_count):
    adapters = sorted(adapters)
    diff = list(map(lambda x: abs(x[0] - x[1]),zip([current_jolt]*len(adapters),adapters)))
    if diff[0] in [1,2,3]:
        jolt_count[diff[0]-1]+=1
        return adapters[0], adapters[1:], jolt_count

jolt_count = [0,0,0]
adapters = list(map(lambda x: int(x.strip()), adapters))
original_adap = adapters
while True:

    if adapters:
        new_jolt, new_adapter, jolt_count = find_adapter(starting_jolt, adapters, jolt_count)
        starting_jolt = new_jolt
        adapters = new_adapter
    else:
        break
print(jolt_count)
print(jolt_count[0]*(jolt_count[-1]+1))

#------------------------------------------part2------------------------------------------------
original_adap.append(0)
original_adap.append(max(original_adap)+3)
original_adap = sorted(original_adap)
connection = []
from itertools import chain
for i in range(len(original_adap)):
    if i == (len(original_adap) -1):
        break
    current_jolt = original_adap[i]
    possible_next_jolts = list(map(lambda x: x[0]+x[1], zip([current_jolt]*3,[1,2,3])))
    actaul_jolts = set(original_adap[i+1:i+4]) & set(possible_next_jolts)
    a = list(chain.from_iterable(connection))
    if not len(set(a) & actaul_jolts):
        connection.append(list(actaul_jolts))


def is_valid(n):
    for i,j in zip(n, n[1:]):
        if not abs(i-j) in [1,2,3]:
            return False
            break
    return True
import itertools
def possible_connect(n1,n,n2):
    total = 0
    n = sorted(n)
    local_list = [n[0],n[1],n[2],n[0:2],n[1:],[n[0],n[-1]]]
    for l in local_list:
        try:
            _n = n1 +list(l)+n2
        except:
            _n = n1 +list([l])+n2

        if is_valid(_n):
            total+=1
    return total+1

prod = []
if connection[0] != 0:
    connection.insert(0,[0])
for i in range(len(connection)):
    if len(connection[i]) > 2:
        total = possible_connect(connection[i-1],connection[i],connection[i+1])
        prod.append(total)
    elif len(connection[i]) == 2:
        prod.append(2)
import numpy as np
print(np.prod(prod))
