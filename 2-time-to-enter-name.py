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

# prints the time you took along with your name
print('Hello {} you took {} seconds to enter your name'.format(x,c))
