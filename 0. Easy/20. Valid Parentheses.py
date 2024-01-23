class Solution:
    def isValid(self, s: str) -> bool:
        stack: list = []
        mapping: dict[str, str] = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False
        return len(stack) == 0
