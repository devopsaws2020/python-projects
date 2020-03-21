# Importing the time module 
import time 

# setting the variable named a to be the current time since epoch 
a=time.time() 

# pausing the program for 10 seconds 
time.sleep( 10 ) 

# setting the variable b to be the current time since epoch
b=time.time() 


# subtracting a from b and setting the value to variable c 
c=b-a

# printing the value of c 
print(c)
