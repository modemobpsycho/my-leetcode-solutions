class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res: dict = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in res.keys():
                if s[i] not in res.values():
                    res[pattern[i]] = s[i]
                else:
                    return False
            elif res[pattern[i]] != s[i]:
                return False
        return True
