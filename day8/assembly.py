with open('input.txt', 'r') as r:
    assembly_code = r.readlines()
import operator
ops = {"+": operator.add, "-": operator.sub}
ip = 0
acc = 0
visited = []

def get_instruction(ins):
    ins = ins.split(' ')
    return ins
"""

while True:
    ins =  get_instruction(assembly_code[ip].strip())
    if ip not in visited:
        visited.append(ip)
    else:
        break
    if ins[0] == "jmp":
        ip = ops[ins[1][0]](ip, int(ins[1][1:]))
    elif ins[0] == "acc":
        acc = ops[ins[1][0]](acc, int(ins[1][1:]))
        ip += 1
    else:
        ip += 1
"""
#----------------------part2----------------------------------------
with open('input.txt', 'r') as r:
    assembly_code = r.readlines()
import operator
ops = {"+": operator.add, "-": operator.sub}
ip = 0
acc = 0
visited = []
def get_instruction(ins):
    ins = ins.split(' ')
    return ins
while True:
    ins =  get_instruction(assembly_code[ip].strip())
    if ip not in visited:
        visited.append(ip)
    else:
        max_reach = max(visited)
        break

    if ins[0] == "jmp":
        ip = ops[ins[1][0]](ip, int(ins[1][1:]))
    elif ins[0] == "acc":
        acc = ops[ins[1][0]](acc, int(ins[1][1:]))
        ip += 1
    else:
        ip += 1

def change_assembly_code(ip):
    max_reach = ip
    if get_instruction(assembly_code[max_reach])[0] == "jmp":

        assembly_code[max_reach] = assembly_code[max_reach].replace( "jmp", "nop")
    else:
        assembly_code[max_reach] = assembly_code[max_reach].replace( "nop", "jmp")
    return assembly_code

def check_assembly(assembly):
    ip = 0
    acc = 0
    visited = []

    while True:
        try:
            ins =  get_instruction(assembly[ip].strip())
        except:
            break
        if ip not in visited:
            visited.append(ip)
        else:
            break
        if ins[0] == "jmp":
            ip = ops[ins[1][0]](ip, int(ins[1][1:]))
        elif ins[0] == "acc":
            acc = ops[ins[1][0]](acc, int(ins[1][1:]))
            ip += 1
        else:
            ip += 1
    return ip,acc


for ip in reversed(visited):
    if get_instruction(assembly_code[ip])[0] in ("jmp","nop"):
        assembly_code_new = change_assembly_code(ip)
        ip_new, acc_new = check_assembly(assembly_code_new)
        if  ip_new == len(assembly_code):
            print(ip_new, acc_new)
            break

