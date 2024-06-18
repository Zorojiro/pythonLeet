class Solution:
    def maxProfitAssignment(self, diff: List[int], profit: List[int], worker: List[int]) -> int:
        n = max(diff)

        map = [0 for i in range(n+1)]

        for i in range(0,len(diff)):
            map[diff[i]] = max(map[i], profit[i])

        for i in range(1, n+1):
            map[i] = max(map[i], map[i-1])
        
        totalPro = 0
        for i in worker:
            if i > n:
                totalPro += map[n]
            else:
                totalPro += map[i]
        
        return totalPro


        
        