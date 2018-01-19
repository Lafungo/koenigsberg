# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:01:47 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def coins_comb(n, coins, max_coin):
    if n < 0 or max_coin < 0:
        return 0
    
    if n == 0 or max_coin == 0:
        return 1
    
    s = 0
    
    for m in range(n // coins[max_coin] + 1):
        s += coins_comb(n - (m * coins[max_coin]), coins, max_coin - 1)
    
    return s

#def coins_comb(n, coins, max_coin):
#    if n < 1 or max_coin < 0:
#        return 0
#    
#    if n == 1 or max_coin == 0:
#        return 1
#    
#    while coins[max_coin] > n:
#        max_coin -= 1
#        
#    s = 1
#    
#    for coin in range(1, max_coin):
#        for m in range(1, (n // coins[coin]) + 1):
#            s += coins_comb(n - (m * coins[coin]), coins, max_coin - 1)
#            
#    if n in coins:
#        s += 1
#    
#    return s

print(coins_comb(200, coins, 7))

end = datetime.datetime.now()
print(end - start)
