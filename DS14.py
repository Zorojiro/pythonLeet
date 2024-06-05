class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = set()
        length = 0

        for char in s:
            if char in map:
                map.remove(char)
                length += 2
            else:
                map.add(char)

        if map:
            length += 1

        return length
