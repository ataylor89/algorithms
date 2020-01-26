class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        maxLength = int(len(s)/2)
        sLength = len(s)
        
        for length in range(1, maxLength+1):
            if sLength % length != 0:
                continue
                
            b = True
            n = 0
            
            while b == True and (n+2)*length <= sLength:
                if s[n*length:(n+1)*length] != s[(n+1)*length:(n+2)*length]:
                    b = False
                n += 1
            
            if b == True:
                return True
        
        return False
