class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c**0.5)
        
        while i<=j:
            Sum = i**2 + j**2
            if Sum == c:
                return True
            elif Sum < c:
                i+=1
            else:
                j-=1
        return False
        