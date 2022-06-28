#!/usr/bin/python3                                                              
import random
number = random.randint(-10000, 10000)
if number[-1] == 0:
    var_1 = "and is zero"
    print(f"Last digit of {number} is {number[-1]} + {var_1}")                  elif number[-1] > 5:
        var_1 = "and is greater than 5"
        print(f"Last digit of {number} is {number[-1]} + {var_1}")              elif number[-1] < 6 and number[-1] != 0:
            var_1 = "and is less than 6 and not 0"
            print(f"Last digit of {number} is {number[-1]} + {var_1}")
