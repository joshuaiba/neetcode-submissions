class Solution:
    def isValid(self, s: str) -> bool:
        p = {"}" : "{" ,")" : "(", "]" : "["}
        stack = []
        for c in s:
            if c in p:
                if not stack or stack[-1] != p[c]:
                    return False
                stack.pop()
            else:
                 stack.append(c)
        return len(stack) == 0
        