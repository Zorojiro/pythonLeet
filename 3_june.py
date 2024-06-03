class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_size =len(t)
        s_size = len(s)
        ti ,si = 0,0

        while ti<t_size and si<s_size:
            if s[si] == t[ti]:
                ti+=1
            
            si+=1
        return t_size - ti;  
        