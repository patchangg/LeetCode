
def reformat(s):
    output = ""
    if s.isalnum():
        letters = []
        numbers = []
        for c in s:
            if c.isalpha():
                letters.append(c)
            else:
                numbers.append(c)
        if abs(len(letters) - len(numbers)) > 1:
            return output
        for i in range(ceil(len(s) / 2)):
            if len(letters) > len(numbers):
                output += (letters[i])
                if i < len(numbers):
                    output += (numbers[i])
            else:
                output += (numbers[i])
                if i < len(letters):
                    output += (letters[i])
    return output

s = "a0b1c2"
reformmatedString = reformat(s)
print(reformmatedString)
