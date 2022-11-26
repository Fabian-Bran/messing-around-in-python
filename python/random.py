import random
import time

rando = random.randint(0, 100)
stop = 1
while stop != 7:
    if stop == 1:
        print("the first number is", rando)
        rando = random.randint(0,100)
        stop += 1
        time.sleep(0.5)
    elif stop == 6:
            print("the last number is ", rando)
            rando = random.randint(0,100)
            stop += 1
            time.sleep(0.5)
    else:
        print("the next number is ", rando)
        rando = random.randint(0,100)
        stop += 1
        time.sleep(0.5)

