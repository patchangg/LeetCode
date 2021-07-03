
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    output = [0] * len(temperatures)
    stack = []
    for i,t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            output[cur] = i - cur
        stack.append(i)
    return output

# Use a stack to compare the index position to the current positions temperature
# if the current position temperate is greater than the index
# calculate the position different and put it in the results.
# O(n*m) where n is the length of temperatures and m is the while loop stack
temperatures = [73,74,75,71,69,72,76,73]
days = dailyTemperatures(temperatures)
print(days)
