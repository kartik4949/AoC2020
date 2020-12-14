with open('account.txt', 'r') as r:
    account = r.readlines()
    account = list(map(lambda x: int(x.strip()), account))

import itertools
price1 = [p1*p2 for p1, p2 in itertools.product(account, account) if p1+p2 == 2020][0]
price2 = [p1*p2*p3 for p1, p2, p3 in itertools.product(account, account, account) if p1+p2+p3 == 2020][0]
print(price1,price2)
