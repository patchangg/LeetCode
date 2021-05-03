
def reverseWords(s):
    array = s.split(" ")
    reversed = []
    for word in array:
        reversed.append(word[::-1])
    return " ".join(reversed)


s = "Let's take LeetCode contest"
reversed = reverseWords(s)
print(reversed)
