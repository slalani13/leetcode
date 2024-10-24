class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        i=0
        new_path = path.split('/')
        print(new_path)
        while i < len(new_path):
            if new_path[i] == "":
                i += 1
            elif new_path[i] == ".":
                i += 1
            elif new_path[i] == "..":
                if stk:
                    stk.pop()
                if stk:
                    stk.pop()
                i += 1
            else:
                stk.append("/")
                stk.append(new_path[i])
                i += 1
        res = "".join(stk)
        if res == "":
            return "/"
        return res