with open("input.txt") as r:
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
                if number >= rang[0] and number <= rang[1]:
                    bad_nums.append(True)
                    break
        if not any(bad_nums):
            not_in_range.append(number)
    return sum(not_in_range), len(not_in_range)


for d in data:
    if d == "\n":
        total_data.append(data_seperated)
        data_seperated = []
        continue
    if ":" in d:
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
        f = f.split("-")
        tf.append(list(map(int, f)))

    fields.append(tf)
near_ticket = []
elements = 0
tickets = []
for ticket in total_data[-1][1:]:
    ticket = ticket.strip().split(",")
    sum_data, len_data = check_for_bad_data(ticket)
    elements+=sum_data
    if not len_data:
        tickets.append(ticket)
fields = []
for field in total_data[0]:
    tf = []
    for f in field:
        f = f.strip()
        f = f.split("-")
        tf.append(list(map(int, f)))

    fields.append(tf)
int_fields = fields
near_ticket = []

visited = []

def filter_func(x, f):
    if (x>=f[0][0] and x<=f[0][1]) or (x>=f[1][0] and x<=f[1][1]):
        return False
    else:
        return True

def check_field_related(ticket_vert):
    temp = []
    for i, f in enumerate(int_fields):
        not_in_range = list(filter(lambda x: filter_func(x, f), map(int, ticket_vert)))
        if not len(not_in_range):
            temp.append(i)
    return temp

ordered_fields = []
vertical_tickets = []
valid_per_column= []
for i in range(len(tickets[0])):
    temp_v_t = []
    for ticket in tickets:
        temp_v_t.append(ticket[i])
    #ordered_fields.append(check_field_related(temp_v_t))
    valid = check_field_related(temp_v_t)
    valid_per_column.append(valid)
valid_fields = []
for i,v in enumerate(valid_per_column):
    valid_fields.append([i,v])
for i in sorted(valid_fields, key=lambda k:len(valid_fields[k[0]][1])):
    for j in valid_fields:
        if i[0] != j[0]:
            try:
                j[1].remove(i[1][0])
            except:
                continue
valid_field = [i[1][0] for i in valid_fields]
import numpy as np
your_ticket = list(map(int, total_data[1][1].strip().split(',')))
j=0
prod = 1
for i in valid_field:
    if i<6:
        prod*=your_ticket[j]
    j+=1
print("part1", elements)
print("part2",prod)
