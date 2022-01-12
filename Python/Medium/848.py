
def shiftingLetters(s, shifts):
    string = [c for c in s]
    for i in range(len(shifts)-2,-1,-1):
        shifts[i] += shifts[i+1]
    for i in range(len(shifts)):
        if ord(string[i]) + shifts[i] > ord('z'):
            string[i] = chr((ord(string[i]) - 97 + shifts[i]) % 26 + 97)
        else:
            string[i] = chr(ord(string[i])+shifts[i])
    return "".join(string)

# Turn the string into a character array and do a suffix sum for the shifts
# For each letter, add the shifts and if it is over z or 122, wrap the number
# around to get the letter. O(n), O(n) space
s = "abc"
shifts = [3,5,9]
shiftedString = shiftingLetters(s,shifts)
print(shiftedString)
