from collections import defaultdict
with open("input.txt") as r:
    adapter = r.readlines()
addapters = [0] + sorted(map(int,adapter ))
addapters.append(addapters[-1] + 3)

diffs = defaultdict(int)
counts = defaultdict(int, {0: 1})

for a, b in zip(addapters[1:], addapters):
    diffs[a - b] += 1
    # number of ways to reach i'th adapter from previous three possible ones
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]

print(diffs[1] * diffs[3])
print(counts[addapters[-1]])
