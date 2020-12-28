def conv_binary_36(number):
    return bin(number)

def apply_mask(binary, mask):
    binary = list('0'*(36 - len(binary[2:])) + binary[2:])
    for m in mask:
        binary[m[1]] = m[0]
    return "".join(binary)

with open('input.txt') as r:
    bins = r.readlines()
masks = []
def mask(mask):
    breakpoint()
    for i in range(len(mask)):
        if mask[i] != "X":
            masks.append((mask[i], i))
    return masks
memory = {}
import re
for bini in bins:
    print(bini)
    if "mask" in bini:
        masks = mask(bini.strip().split(" = ")[-1])
    else:
        number = int(bini.strip().split(" = ")[-1])
        binary = apply_mask(conv_binary_36(number), masks)
        number = re.findall("\[(.*?)\]", bini.strip().split(" = ")[0])
        print(number)
        memory[number[0]] = int(binary,2)
breakpoint()
print(sum(memory.values()))
