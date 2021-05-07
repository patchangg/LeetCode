
def removeDuplicates(S):
    stack = []
    for i in S:
        if len(stack) != 0:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    return "".join(stack)


S = "abbaca"
removed = removeDuplicates(S)
print(removed)
