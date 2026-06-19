class Solution(object):
    def isValid(self, s):

        bracket = []

        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:
            if ch in "({[":
                bracket.append(ch)

            else:
                if not bracket or bracket[-1] != mapping[ch]:
                    return False
                
                bracket.pop()
        
        return len(bracket) == 0