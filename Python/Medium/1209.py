
def removeDuplicates(s, k):
    stack = [['!',0]]
    for char in s:
        if stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1]== k:
                stack.pop()
        else:
            stack.append([char,1])
    return ''.join(c * i for c, i in stack)

# Create a stack and count the occurance of the character in the string
# if the current character is the same as the previous, add to it
# if it isn't, add it to the stack.
# If the occurance = k then remove it from the stack
# Join the remaining characters in the stack and return it
s = "abcd"
k = 2
finalString = removeDuplicates(s,k)
print(finalString)
