
def numTeams(rating):
    output = 0
    for index,middle in enumerate(rating):
        mgl = mll = mgr = mlr = 0
        for left in rating[:index]:
            if left < middle:
                mgl += 1
            elif left > middle:
                mll += 1
        for right in rating[index+1:]:
            if right > middle:
                mlr += 1
            elif right < middle:
                mgr += 1
        output += mlr * mgl
        output += mgr * mll
    return output

# works by checking l<m<r pairs and l>m>r pairs for each element in rating
# use the first loop as the middle to use less loops'
# left loop checks how many elements are smaller than the middle, vice versa for right loop
# multiply them for the amount of different combinations you can acheive
#rating = [2,5,3,4,1]
#rating = [2,1,3]
rating = [1,2,3,4]
number = numTeams(rating)
print(number)
