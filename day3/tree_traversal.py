with open('input.txt', 'r') as r:
    map_data = r.readlines()
def split(word):
    return [char for char in word]
# -------------------- part 1 ---------------------------------#
def tree_traversal(slope):
    x, y = slope
    lane_idx = 0
    tree_count = 0
    while True:
        try:
            lane = map_data[lane_idx]
        except:
            break
        location = lane[(int(lane_idx/y)*x)%31]
        if location == '#':
            tree_count += 1
        lane_idx += y
    return tree_count
print(tree_traversal((3,1)))



# -------------------- part 2 ---------------------------------#
tree_per_maps = list(map(tree_traversal, [(1,1), (3,1), (5,1), (7,1), (1, 2)]))
mul_tree_result = 1
for trees in tree_per_maps:
    mul_tree_result*=trees
print(mul_tree_result)


