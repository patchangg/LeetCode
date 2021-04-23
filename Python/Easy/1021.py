
def removeOuterParentheses(S):
    stack = []
    counter = 0
    for i in S:
        if i == "(":
            counter += 1
            if counter == 1:
                pass
            else:
                stack.append(i)
        elif i == ")":
            counter -= 1
            if counter == 0:
                pass
            else:
                stack.append(i)
    return ''.join(stack)

S = "()()"
outer = removeOuterParentheses(S)
print(outer)
