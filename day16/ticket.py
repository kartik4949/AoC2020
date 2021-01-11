with open('input.txt') as r:
    data = r.readlines()
fields = []
your_ticket = []
near_ticket = []
data_seperated = []
total_data = []

def check_for_bad_data(ticket):
    not_in_range = []
    for number in ticket:
        number = int(number)
        bad_nums = []
        for field in fields:
            if any(bad_nums):
                break
            for rang in field:
                if (number>=rang[0] and number<=rang[1]):
                    bad_nums.append(True)
                    break
        if not any(bad_nums):
            not_in_range.append(number)
    return sum(not_in_range)


for d in data:
    if d == "\n":
        total_data.append(data_seperated)
        data_seperated = []
        continue
    if ':' in d:
        d = d.strip()
        d = d.split(":")[-1]
        d = d.split(" or ")
    data_seperated.append(d)
else:
    total_data.append(data_seperated)
fields = []
for field in total_data[0]:
    tf = []
    for f in field:
        f = f.strip()
        f = f.split('-')
        tf.append(list(map(int, f)))

    fields.append(tf)
near_ticket = []
elements = 0
for ticket in total_data[-1][1:]:
    ticket = ticket.strip().split(',')
    elements += check_for_bad_data(ticket)

print(elements)
