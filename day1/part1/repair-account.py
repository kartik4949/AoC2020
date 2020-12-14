with open('account.txt', 'r') as r:
    account = r.readlines()
    account = list(map(lambda x: int(x.strip()), account))

import itertools
price = [p1*p2 for p1, p2 in itertools.product(account, account) if p1+p2 == 2020][0]
print(price)
