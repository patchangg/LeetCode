
def isValidSerialization(preorder):
    preorder = preorder.split(',')
    slots = 1

    for p in preorder:
        slots -= 1
        if slots < 0:
            return False
        if p != "#":
            slots += 2

    return slots == 0

# Split the string by ',' to get each individual character
# Slots = 1 for the root node and to account for [#,]
# Remove a slot each interval, if the slot isn't a null value, add 2 slots as
# it has two more neighbours. If slots == 0, that means the tree is in
# pre-order. O(n), O(n) space
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
validTree = isValidSerialization(preorder)
print(validTree)
