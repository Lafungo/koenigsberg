# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:12:51 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

coins = [c for c in range(1, 101)]

def coins_comb(n, coins, max_coin):
    if n < 0 or max_coin < 0:
        return 0
    
    if n == 0 or max_coin == 0:
        return 1
    
    s = 0
    
    for m in range(n // coins[max_coin] + 1):
        s += coins_comb(n - (m * coins[max_coin]), coins, max_coin - 1)
    
    return s

print(coins_comb(100, coins, 99) - 1)

end = datetime.datetime.now()
print(end - start)
