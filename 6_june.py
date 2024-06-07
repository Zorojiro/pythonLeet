class Solution:
    def nextOne(self, hand, grpsize, i, n):
            nextNum = hand[i] + 1
            hand[i] = -1
            count = 1
            i+=1
            while i<n and count < grpsize:
                if hand[i] == nextNum:
                    nextNum = hand[i] + 1
                    hand[i] = -1
                    count += 1
                i+=1
            
            return count == grpsize

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        hand.sort()
        for i in range(n):
            if hand[i] >= 0:
                if not self.nextOne(hand, groupSize, i, n):
                    return False
        
        return True

        