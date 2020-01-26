from collections import defaultdict
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        
        g.sort()
        s.sort()
        
        n = 0
        
        for greedFactor in g:
            sizeFound = -1
            for size in s:
                if size >= greedFactor:
                    n += 1
                    sizeFound = size
                    break
            if sizeFound > 0:
                s.remove(sizeFound)
        
        return n
