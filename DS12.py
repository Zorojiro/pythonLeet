# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=0,n
        ans = 0
        while left<=right:
            mid=(left+right)//2
            if isBadVersion(mid)==True:
                ans = mid
                right=mid-1
            else:
                left=mid+1
        return ans
            


        