class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        
        n = 0
        
        while z > 0:
            if z & 1 > 0:
                n += 1
            
            z = z >> 1
        
        return n
