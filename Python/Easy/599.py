
def findRestaurant(list1, list2):
    output = []
    lis = float('inf')
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if i+j < lis:
                    lis = i+j
                    output = []
                    output.append(list1[i])
                elif i+j == lis:
                    output.append(list1[i])
    return output

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
commonStringsLIS = findRestaurant(list1,list2)
print(commonStringsLIS)
