class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        count = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left = left + 1
            right = right - 1
            count = count + 1
        
        return count
        