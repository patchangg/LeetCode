
def closestDivisors(num):
    for i in range(int((num+2)**0.5),0,-1):
        if ((num+1) % i) == 0:
            return [i,int((num+1)/i)]
        if ((num+2) % i ) == 0:
            return [i,int((num+2)/i)]

# Need to find two integers whose product equals num + 1 or num + 2
# So we go from Sqrt(num) to 0 to find a integer that divides n+1 or n+2
# which will get a valid pair whose products equals num + 1 or num + 2
# O(sqrt(n)), O(1) space
num = 8
closest = closestDivisors(num)
print(closest)
