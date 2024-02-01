from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram: dict = {}

        for word in strs:
            temp_word: str = "".join(sorted(word))

            if temp_word in anagram:
                anagram[temp_word].append(word)

            else:
                anagram[temp_word] = [word]

        return list(anagram.values())
