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




validators = {'byr':{'limit':4, 'range':[1920, 2002]},
'iyr':{'limit':4, 'range':[2010, 2020]},
'eyr':{'limit':4, 'range':[2020, 2030]},
'hgt':{'post_fix':['cm','in'], 'cm_range':[150,193], 'in_range':[59,76]},
'hcl':{'pre_fix':'#', 'limit':6, 'valid':[(0,9), ('a','f')]},
'ecl':{'valid':['amb' ,'blu' ,'brn' ,'gry' ,'grn' ,'hzl', 'oth']},
'pid':{'limit':9}}

def validate_field(field):
    key, value = field
    validator = validators[key]
    for validate,valid in validator.items():
        if 'range' in validate:
            try:
                value = int(value)
            except:
                validate = validate.split('_')[0]
                value_post = value[-len(validate):]
                value_pre = int(value[:-len(validate)])
                if (validate == value_post):
                    if not (value_pre>=int(valid[0]) and value_pre<=int(valid[1])):
                        return False
            else:
                if not (value>=valid[0] and value<=valid[1]):
                    return False
        elif 'limit' in validate:
            try:
                int(value)
            except:
                if len(value[1:]) != valid:
                    return False
            else:
                if len(value)!=valid:
                    return False
        elif 'pre' in validate:
            if not value[0] == valid:
                return False
        elif 'post' in validate:
            if not value[-len(valid):] in valid:
                return False
        elif 'valid' in validate:
            if any([isinstance(t, tuple) for t in valid]):
                value = value[1:]
                try:
                    int(value)
                except:
                    for v in value:
                        try:
                            int(v)
                        except:
                            if not (ord(v) >= 97 and ord(v) <= 102):
                                return False
            else:
                if not value in valid:
                    return False
    return True

with open('input.txt', 'r') as r:
    passports = r.readlines()


valids = 0

def check_fields(passport):
    fields = []
    data = passport.strip().split(' ')
    for d in data:
        if d.split(':')[0] != 'cid':
            fields.append(d.split(':'))
    return fields
fields = []
passports.append('\n')
for i, passport_line in enumerate(passports):
    if passport_line == "\n":
        valid_field = True
        valid = check_password(fields)
        for field in fields:
            if not validate_field(field):
                valid_field= False
                break
        if valid and valid_field:
            valids+=1
        fields = []
    else:
        fields += check_fields(passport_line)
print(valids)

