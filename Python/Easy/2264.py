
def largestGoodInteger(num):
    largest = ["999","888","777","666","555","444","333","222","111","000"]
    for n in largest:
        if n in num:
            return n
    return ""

num = "6777133339"
goodInteger = largestGoodInteger(num)
print(goodInteger)
