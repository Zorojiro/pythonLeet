class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k = -1
        nums_set = set(nums)
        for n in nums:
            if n > 0:
                if n > k and -n in nums_set:
                    k = n


        return k