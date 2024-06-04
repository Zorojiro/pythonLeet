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


        """
        'a' is not in the set. Add 'a'. Set: {'a'}
        'b' is not in the set. Add 'b'. Set: {'a', 'b'}
        'c' is not in the set. Add 'c'. Set: {'a', 'b', 'c'}
        Another 'c'. It's already in the set. Remove 'c'. Increase length by 2. Length: 2. Set: {'a', 'b'}
        """