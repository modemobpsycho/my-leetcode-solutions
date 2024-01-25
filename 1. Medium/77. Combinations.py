from typing import List


def combinationSum(n) -> list:
    results = []
    helper(n, [], 1, results)
    return results


def helper(target, combination, start, results) -> None:
    if target == 0:
        results.append(combination)
        return
    if target < 0:
        return

    for i in range(start, target + 1):
        helper(target - i, combination + [i], i, results)


n = 5
results = combinationSum(n)
for combination in results:
    print(combination)
