
def longestMountain(arr):
    up = [0] * len(arr)
    down = [0] * len(arr)
    mountain = [0]
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            up[i] = up[i-1] + 1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > arr[i+1]:
            down[i] = down[i+1] + 1
    for u, d in zip(up,down):
        if u and d:
            mountain.append(u+d+1)
    return max(mountain)

# Do two passes of the arr array, one forward capturing the length of height
# increases and one backwards capturing the length of height decreases.
# Go through both capture arrays and find any points where both index values
# are positive, this means that at this point, it goes up and down on the sides
# which indicates a mountain, store the length and return the maximum length found.
# O(3n) = O(n), O(n) space
arr = [2,1,4,7,3,2,5]
mountainSize = longestMountain(arr)
print(mountainSize)
