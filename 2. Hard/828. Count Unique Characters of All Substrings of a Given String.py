from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        inds = defaultdict(lambda: [-1])
        for i, ch in enumerate(s):
            inds[ch].append(i)
        
        res = 0
        for v in inds.values():
            v.append(len(s))
            for i in range(1, len(v)-1):
                res += (v[i] - v[i-1]) * (v[i+1] - v[i])
        return res