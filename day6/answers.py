with open('input.txt') as r:
    answers = r.readlines()

count = 0
counts = []
total_counts = []
answers.append('\n')
for group in answers:
    if group == "\n":
        if len(counts) == 1:
            total_counts.append(len(counts[0]))
        else:
            count = len(set(counts[0]).intersection(*counts))
            total_counts.append(count)
        counts = []
    else:
        group = group.strip()
        counts.append([g for g in group])
print(sum(total_counts))
