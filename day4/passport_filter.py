with open('input.txt', 'r') as r:
    passports = r.readlines()

def check_fields(passport):
    fields = []
    data = passport.strip().split(' ')
    for d in data:
        if d.split(':')[0] != 'cid':
            fields.append(d.split(':')[0])
    return fields
def check_password(fields):
    if len(fields) == 7:
        return True
    else:
        return False

valids = 0
fields = []
passports.append('\n')
for i, passport_line in enumerate(passports):
    if passport_line == "\n":
        valid = check_password(fields)
        if valid:
            valids+=1
        fields = []
    else:
        fields += check_fields(passport_line)
print(valids)
