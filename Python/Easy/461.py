
def hammingDistance(x, y):
    # xbit = "{0:b}".format(x)[::-1]
    # ybit = "{0:b}".format(y)[::-1]
    # print(xbit,ybit)
    # xpos = 0
    # ypos = 0
    # for i in range(len(xbit)):
    #     if xbit[i] == "1":
    #         xpos = i
    # for s in range(len(ybit)):
    #     if ybit[s] == "1":
    #         ypos = s
    # return abs(xpos - ypos)
    print(bin(x ^ y).count("1"))


x = 4
y = 1
distance = hammingDistance(x,y)
print(distance)
