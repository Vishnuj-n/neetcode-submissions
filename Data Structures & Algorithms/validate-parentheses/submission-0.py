class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        clossing={"}":"{",")":"(","]":"["}
        for i in s:
            if i in clossing:
                if stack and stack[-1]==clossing[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0