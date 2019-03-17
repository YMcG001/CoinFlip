#Coin Flip Program
#Flips coin 100 times.  Tells you # of heads and # of tails.

import random

def flip():
    random.randint(1,2)
    heads=0
    tails=0

for i in range(100):
    flip()
    if flip == 1:
        heads += 1
        print(heads)
    if flip == 2:
        tails += 1
        print(tails)

print("Total:\n ", heads, "were heads and...")
print(tails, " were tails.")

input("\n\nPress Enter to Exit")
