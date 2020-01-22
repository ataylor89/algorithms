# The add function is contributed by Smitha Dinesh Semwal 
# https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/

def _add(x, y): 
  
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

def _subtract(x, y):

    while (y != 0):
    
       borrow = (~x) & y

       x = x ^ y

       y = borrow << 1

    return x
 
def add(x, y):
    
    if x >= 0 and y >= 0:
        return _add(x, y)

    if x >= 0 and y < 0:
        if -y > x:
            return -_subtract(-y, x)
        else:
            return _subtract(x, -y)

    if x < 0 and y >= 0:
        if -x > y:
            return -_subtract(-x, y)
        else:
            return _subtract(y, -x)

    if x < 0 and y < 0:
        return -_add(-x, -y)

 
print("15  +   32 = " + str(add(15, 32)))
print("30  +  -15 = " + str(add(30, -15)))
print("10  +  -15 = " + str(add(10, -15)))
