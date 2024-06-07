class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        j = 0
        maxLen = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[j])
                j+=1

            charSet.add(s[i])
            maxLen = max(maxLen, i-j+1)
        
        return maxLen
        