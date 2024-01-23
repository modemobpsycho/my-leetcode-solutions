class Solution:
    def checkRecord(self, s: str) -> bool:
        l_cnt = 0
        a_cnt = 0

        for c in s:
            if c == "A":
                a_cnt += 1
                if a_cnt == 2:
                    return False

            if c == "L":
                l_cnt += 1
                if l_cnt > 2:
                    return False
            else:
                l_cnt = 0

        return True
