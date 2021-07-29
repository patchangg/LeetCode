
def shipWithinDays(self, weights: List[int], days: int) -> int:
    low = max(weights) # 10
    high = sum(weights) # 55
    while low < high:
        middle = (low + high) // 2
        total = 0
        result = 1
        for weight in weights:
            if total + weight > middle:
                result += 1
                total = weight
            else:
                total += weight
        if result <= days:
            high = middle
        else:
            low = middle + 1
    return low

# Use a binary search to find the minimum amount of ship weight to
# deliver the cargo in x days
# To get exactly D days we need to bound the binary search [max(w),sum(w)]
# and do a binary search until low is >= to high which means they should equal
# This results in finding the minimum weight to deliver in days.
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
shipment = (weights,days)
print(shipment)
