
def sumFourDivisors(nums):
    output = 0
    for num in nums:
        divisors = set()
        for i in range(1,floor(sqrt(num))+1):
            if num % i == 0:
                divisors.add(num//i)
                divisors.add(i)
            if len(divisors) > 4:
                break
        if len(divisors) == 4:
            output += sum(divisors)
    return output

# Go through each number in nums and loop until the square root of the number
# finding any number that divides it. If a number divides it, put the num divided
# by the divisor and the divisor in a set. If the length of the set is greater
# than four, break the loop as only look for four. If only four divisors exist
# for the number, add the sum to the output. O(nlogn), O(n) space
nums = [21,4,7]
fourDivisors = sumFourDivisors(nums)
print(fourDivisors)
