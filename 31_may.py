class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)  
        ans = [num for num, freq in count.items() if freq == 1]  
        return ans