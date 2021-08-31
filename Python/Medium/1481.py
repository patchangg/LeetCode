from collections import Counter

def findLeastNumOfUniqueInts(arr, k):
    frequency = Counter(arr)
    removed = 0
    for i in frequency.most_common()[::-1]:
        if k - i[1] > 0:
            k -= i[1]
            removed += 1
        elif k - i[1] == 0:
            removed += 1
            break
        elif k - i[1] < 0:
            break
    return len(set(arr)) - removed

# Count the frequency of each integer in the array and then loop through it
# from lowest to highest.
# If k - frequency of the integer is greater than 0, remove it from k, add one to counter
# If k - frequency of the integer is equal to 0, add one to coutner and break the loop
# If k - frequency of the integer is less than 0, break the loop
# Transform the array into the set and return the length of the set minus the counter
# to get how many unique integers remain in the array. O(n), O(1) space
arr = [5,5,4]
k = 1
uniqueNumbers = findLeastNumOfUniqueInts(arr,k)
print(uniqueNumbers)
