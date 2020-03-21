# importing the time module
import time


# Print asking you to enter your name
print('Enter your name:')

# Recordin the time before the question is asked
a=time.time()

# this line will take what you type as input
x = input()

# record the time when you enter your time
b=time.time()

# calculates the time you took to enter your name
c=b-a

d=round(c,2)


# if your time is less than 3 seconds= fast, 4-8 seconds = medium , more than 8 seconds = slow

if d <=3:
    person="fast"
elif d >3 and d<8:
    person="medium"
else:
    person="slow"


# prints the time you took along with your name
print('Hello {} you took {} seconds to enter your name. Your typing speed is {}'.format(x,d,person))
