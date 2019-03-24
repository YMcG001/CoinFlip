#Coin Flip Program
#Flips coin 100 times.  Tells you # of heads and # of tails.

import random

def flip():
    return(random.randint(1,2))

heads = 0
tails = 0

for i in range(100):
    flip()
    if flip() == 1:
        heads += 1
    else:
        tails += 1

print("RESULT: \nOut of 100 coin flips... \n",heads, " were Heads. \n",tails, " were Tails.")
    
input("\n\nPress Enter to Exit")
