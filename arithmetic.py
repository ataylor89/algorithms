# The add function is contributed by Smitha Dinesh Semwal 
# https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/

def add(x, y): 
  
    # Iterate till there is no carry  
    while (y != 0): 
      
        # carry now contains common 
        # set bits of x and y 
        carry = x & y 
  
        # Sum of bits of x and y where at 
        # least one of the bits is not set 
        x = x ^ y 
  
        # Carry is shifted by one so that    
        # adding it to x gives the required sum 
        y = carry << 1
      
    return x 

def subtract(x, y):

    while (y != 0):
    
       borrow = (~x) & y

       x = x ^ y

       y = borrow << 1
  
print("15 + 32 = " + str(add(15, 32)))
print("30 - 15 = " + str(subtract(30, 15)))
