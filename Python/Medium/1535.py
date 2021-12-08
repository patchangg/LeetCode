
def getWinner(arr, k):
    if k >= len(arr):
        return max(arr)
    count = 0
    curr = arr[0]
    for i in range(1,len(arr)):
        if curr < arr[i]:
            curr = arr[i]
            count = 0
        count += 1
        if count == k:
            break
    return curr

# If k is longer than the length of the array, the highest number always wins
# So that means if k is less than the length of the array, we only need to do
# one pass of the array to get the winner as there is always a winner.
# So loop through the array, updating the highest number between the first
# and second position until it has won k games. O(n), O(1) space
arr = [2,1,3,5,4,6,7]
k = 2
winner = getWinner(arr,k)
print(winner)
