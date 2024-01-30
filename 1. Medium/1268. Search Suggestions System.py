from typing import List


def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    ans = []
    n: int = len(searchWord)
    l: list[str] = sorted(products)
    for i in range(n):
        pre: str = searchWord[: i + 1]
        t = []
        c = 0
        for j in l:
            if j[: i + 1] == pre:
                t.append("".join(j))
                c += 1
            if c == 3:
                break
        ans.append(t)
    return ans
