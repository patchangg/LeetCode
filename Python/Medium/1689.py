
def minPartitions(n):
    return max(n)


n = "27346209830709182346"
minimum = minPartitions(n)
print(n)
# This question works as you need to find how many 1 * n to make number
# so 9 = 111111111 so then 8 = 111111110, so the min positives to add up
# to n will always be the highest n
