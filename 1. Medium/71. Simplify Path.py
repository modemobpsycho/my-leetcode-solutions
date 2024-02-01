class Solution:
    def simplifyPath(self, path: str) -> str:
        cadenas: list[str] = path.split("/")
        arr: list = []
        for s in cadenas:
            if s != "." and s != ".." and s:
                arr.append(s)
            elif s == "..":
                if arr:
                    arr.pop()

        return "/" + "/".join(arr)
