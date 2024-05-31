class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s) #^ tends for negation
        s=s.lower()
        rev_s = s[::-1]

        if s==rev_s:
            return True
        else:
            return False

        