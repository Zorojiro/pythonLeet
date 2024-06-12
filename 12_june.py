class Solution:
    def swap(self,arr:List[int], a:int, b:int):
        arr[a], arr[b] = arr[b], arr[a]

    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low = 0
        mid = 0
        high = n-1

        while mid<=high:
            if nums[mid] == 0:
                self.swap(nums, mid, low)
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                self.swap(nums, mid, high)
                high-=1


        
        