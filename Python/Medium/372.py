
def superPow(a, b):
    output = 1
    for num in b[::-1]:
        a, output = pow(a,10,1337), pow(a,num,1337) * output % 1337
    return output

# a^b % k = (a%k)(b%k) % k
# Go through digit by digit to get the final number. O(n), O(1) space
a = 2
b = [3]
number = superPow(a,b)
print(number)
