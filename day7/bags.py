with open('input.txt', 'r') as r:
    bag_groups = r.readlines()

class Node:
    parent = None
    childs = tuple()
    def __init__(self, node):
        self.parent = node

nodes = dict()

def deepwalk(node, flag_list):
    node = nodes[node]
    if "shiny gold" in node.childs:
        flag_list.append(1)
        return
    if len(node.childs) > 0:
        [deepwalk(n, flag_list) for n in node.childs]

for bags in bag_groups:
    bags = bags.strip().split(' bags contain ')
    carry_bag = bags[0]
    bags_inside = bags[1].split(',')
    bags_inside = [" ".join(bags.split(' ')[-3:-1]) for bags in bags_inside]
    node = Node(carry_bag)
    node.childs = tuple(bags_inside) if not "no other" in bags_inside else tuple()
    nodes.update({carry_bag:node})

def find_bags():
    count = 0
    for bag, node in nodes.items():
        if "shiny gold" not in bag:
            if "shiny gold" in node.childs:
                count += 1
                continue
            elif len(node.childs):
                for child_node in nodes[bag].childs:
                    flag = []
                    _walk = deepwalk(child_node, flag)
                    if any(flag):
                        count += 1
                        break
    return count
#print(find_bags())
#-------------------------------part2-------------------------------------


with open('input.txt', 'r') as r:
    bag_groups = r.readlines()

class Node:
    parent = None
    childs = tuple()
    def __init__(self, node):
        self.parent = node

nodes = dict()

def deepwalk(amount, node):
    node = nodes[node]
    if node.childs:
        local_amount = 0
        for n in node.childs:
            _amount = deepwalk(*n)
            local_amount += _amount
        amount += amount*local_amount
    if not node.childs:
        return amount
    return amount


for bags in bag_groups:
    bags = bags.strip().split(' bags contain ')
    carry_bag = bags[0]
    bags_inside = list(map(lambda x:x.strip(), bags[1].split(',')))
    bags_inside = [( 0 if 'no other' in bags else int(bags[0])," ".join(bags.split(' ')[-3:-1])) for bags in bags_inside]
    if len(bags_inside) == 1 and bags_inside[0][0] == 0:
        bags_inside = None

    node = Node(carry_bag)
    node.childs = tuple(bags_inside) if bags_inside else None
    nodes.update({carry_bag:node})

def find_bags():
    for bag, node in nodes.items():
        nodes_inside = []
        if "shiny gold" in bag:
            total = 0
            for child in node.childs:
                total += deepwalk(*child)
            print(total)

find_bags()
