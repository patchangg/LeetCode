
def maxTurbulenceSize(arr):
    output = 0
    maximum = 0
    for i in range(len(arr)):
        if i >= 2 and (arr[i-2] > arr[i-1] < arr[i] or arr[i-2] < arr[i-1] > arr[i]):
            maximum += 1
        elif i >= 1 and arr[i-1] != arr[i]:
            maximum = 2
        else:
            maximum = 1
        output = max(output,maximum)
    return output

# Look for hills and valleys in the array. When a string of them are found,
# keep incrementing the counter and once it has stopped, if the two integers
# next to each other are not the same that means a start of a hill or valley is
# there otherwise its a flat plain. O(n), O(1) space
arr = [9,4,2,10,7,8,8,1,9]
maxTurbulence = maxTurbulenceSize(arr)
print(maxTurbulence)
