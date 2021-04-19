candies = [2,3,5,1,3]
extraCandies = 3
def kidsWithCandies(candies, extraCandies):
#def kidsWithCandies(self, candies, extraCandies):
    max = 0
    greatest = []
    for i in candies:
        if i > max:
            max = i
        #greatest[i] = 0
    for i in candies:
        if (i + extraCandies) >= max:
            greatest.append(True)
            #greatest[i] = True
        else:
            greatest.append(False)
            #greatest[i] = False
    return greatest

#gg = kidsWithCandies(self,candies,extraCandies)
gg = kidsWithCandies(candies,extraCandies)
print(gg)
