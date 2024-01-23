class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1: dict = {}
        d2: dict = {}
        for i in range(len(s)):
            if s[i] in d1:
                if d1[s[i]] != t[i]:
                    return False
            else:
                if t[i] in d2 and d2[t[i]] != s[i]:
                    return False
                else:
                    d1[s[i]] = t[i]
                    d2[t[i]] = s[i]

        return True
