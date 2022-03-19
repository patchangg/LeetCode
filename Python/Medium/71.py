
def simplifyPath(path):
    stack = []
    for system in path.split("/"):
        if stack and system == "..":
            stack.pop()
        elif system not in [".", "..", ""]:
            stack.append(system)

    return "/" + "/".join(stack)

# Split the string by "/". If the word is .., pop the stack,
# otherwise if the word is not a ., push it to the stack. O(n), O(n) space
path = "/home/"
simplePath = simplifyPath(path)
print(simplePath)
