
def hammingWeight(n):
    return bin(n).count('1')

n = 00000000000000000000000000001011
numberOfOnes = hammingWeight(n)
print(numberOfOnes)
