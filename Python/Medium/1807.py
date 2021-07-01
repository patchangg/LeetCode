
def evaluate(s, knowledge):
    dicts = {k:v for k,v in knowledge}
    arr = s.split("(")
    output = arr[0]
    for i in range(1,len(arr)):
        string = arr[i].split(")")
        if string[0] in dicts:
            output += dicts[string[0]]
        else:
            output += "?"
        output += string[1]
    return output

# Store knowledge in a dictionary and split s with "("
# This allows us to split the rest of the string with ")" to get the
# parts that need to be checked with the dictionary
# If its in the dict, replace it else "?". O(n)
s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
evaluated = evaluate(s,knowledge)
print(evaluated)
