X = int(input())
bank = 100
result = 0

import math
import decimal

while (True):
    # print("bank = "+str(bank))
    if(bank >= X):
        break
    else:
        tmp = str(bank*0.01)
        tmp = tmp[:tmp.find('.')]
        bank = bank + int(tmp)
        result = result+1

print(result)
