def conv_binary_36(number):
    return bin(number)

def apply_mask(binary, mask):
    binary = list('0'*(36 - len(binary[2:])) + binary[2:])
    for m in mask:
        binary[m[1]] = m[0]
    return "".join(binary)

with open('input.txt') as r:
    bins = r.readlines()
def mask(mask):
    masks = []
    for i in range(len(mask)):
        if mask[i] != "X":
            masks.append((mask[i], i))
    return masks
memory = {}
import re
for bini in bins:
    if "mask" in bini:
        masks = mask(bini.strip().split(" = ")[-1])
    else:
        number = int(bini.strip().split(" = ")[-1])
        binary = apply_mask(conv_binary_36(number), masks)
        number = re.findall("\[(.*?)\]", bini.strip().split(" = ")[0])
        memory[number[0]] = int(binary,2)
print(sum(memory.values()))

#------------------------------------part2-------------------------------------
def mask(mask):
    return list(mask)
with open('input.txt') as r:
    bins = r.readlines()
import itertools 
def floating_memorys(mem_address):
    nx = mem_address.count('X')
    mem_address = list(mem_address)
    i =0
    idx = []
    while True:
        if len(mem_address)==i:
            break
        if mem_address[i]=='X':
            idx.append(i)
        i+=1
    fps = list(itertools.product(*(list(range(2)),)*nx))
    possible_address = []
    for fp in fps:
        temp = mem_address[:]
        for i,j in zip(fp, idx):
            temp[j] = str(i)
        possible_address.append(temp)
    return possible_address

def apply_mask(number, mask):
    for i in range(36):
        if mask[i]=="X":
            number[i]='X'
        elif mask[i]=='1':
            number[i]='1'
    return number

memory = {}
for bini in bins:
    if "mask" in bini:
        masks = mask(bini.strip().split(" = ")[-1])
    else:
        value = int(bini.strip().split(" = ")[-1])
        mem_number = re.findall("\[(.*?)\]", bini.strip().split(" = ")[0])
        mem_number = bin(int(mem_number[0]))
        mem_number = list('0'*(36 - len(mem_number[2:])) + mem_number[2:])
        number = apply_mask(mem_number[:], masks)
        fps = floating_memorys(''.join(number))
        ns = list(map(lambda x: int(''.join(x),2),fps))
        _ = [memory.update({n:value}) for n in ns]

print(sum(memory.values()))




