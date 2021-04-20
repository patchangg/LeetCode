
def countMatches(items, ruleKey, ruleValue):
    matched = 0
    for i in items:
        if ruleKey == "type":
            if i[0] == ruleValue:
                matched +=1
        elif ruleKey == "color":
            if i[1] == ruleValue:
                matched +=1
        else:
            if i[2] == ruleValue:
                matched +=1
    return matched

# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"
items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
matched = countMatches(items,ruleKey,ruleValue)
print(matched)
