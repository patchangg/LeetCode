
def letterCasePermutation(s):
    output = ['']
    for char in s:
        if char.isalpha():
            output = [i+j for i in output for j in [char.upper(), char.lower()]]
        else:
            output = [i+char for i in output]
    return output

# works by checking if the character in the string is a alphanumeric
# if it is append it to each element in the output list as a upper and lowercase letter
# this makes sure that you get every combination. If char is a number, append to all elements  in list
s = "a1b2"
combo = letterCasePermutation(s)
print(combo)
