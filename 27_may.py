class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)

        for x in range(0, n+1):
            count = 0
            for num in nums:
                if num >= x:
                    count = count + 1

            if count == x:
                return x

        return -1 