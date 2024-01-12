class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typing(s):
            stack = []

            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        return typing(s) == typing(t)
