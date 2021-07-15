
def findMinFibonacciNumbers(k):
    fibNums = [0,1]
    n1 = 0
    n2 = 1
    count = 0
    output = 0
    while count < 43:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        fibNums.append(nth)
        count += 1
    for f in reversed(fibNums):
        if k >= f:
            k -= f
            output += 1
        if k <= 0:
            break
    return output

# Generate the fibnums that are lower than 10^9
# Remove the highest fibnum that is smaller or equal to k
# Continue the for loop until k is less than or equal to 0 or completed.
# Return the amount of numbers that k had used to get k
# O(43 + log43) = O(nlogn), O(1) space
k = 19
minFibNums = findMinFibonacciNumbers(k)
print(minFibNums)
