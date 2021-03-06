with open('pass.txt', 'r') as r:
    passwords = [ l.strip().split(' ') for l in r.readlines()]
valid1 = 0
valid2 = 0
# -----------------------part 1-2--------------------------------------- 
for password in passwords:
    _pass_range = tuple(map(int, password[0].split('-')))
    token = password[1][0]
    password = password[-1]

    token_count = password.count(token)
    if token_count >= _pass_range[0] and token_count <= _pass_range[1]:
        valid1 += 1

    p1 = password[_pass_range[0]-1] == token
    p2 = password[_pass_range[1]-1] == token
    if p1!=p2:
        valid2 += 1
print(valid1)
print(valid2)
