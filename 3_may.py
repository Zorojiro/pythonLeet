class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1, n2 = len(version1), len(version2)
        sum1, sum2 = 0, 0
        factor = 10
        
        i = j = 0
        while i < n1 or j < n2:
            while i < n1 and version1[i] != '.':
                sum1 = factor * sum1 + int(version1[i])
                i += 1
            i += 1
            
            while j < n2 and version2[j] != '.':
                sum2 = factor * sum2 + int(version2[j])
                j += 1
            j += 1
            
            if sum1 < sum2:
                return -1
            elif sum1 > sum2:
                return 1
            
            sum1 = sum2 = 0
        
        return 0