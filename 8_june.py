class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0: -1}  
        sum = 0

        for i, num in enumerate(nums):
            sum += num
            rem = sum % k

            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False