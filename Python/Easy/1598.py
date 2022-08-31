
def minOperations(self, logs: List[str]) -> int:
    stack = []
    for log in logs:
        if log == "../" and stack:
            stack.pop()
        elif log == "../" and not stack:
            continue
        elif log == "./":
            continue
        else:
            stack.append(log)
    return len(stack)

logs = ["d1/","d2/","../","d21/","./"]
numOperationsToGoMain = minOperations(logs)
print(numOperationsToGoMain)
