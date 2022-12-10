
def isPrefixString(s, words):
    output = ""
    for w in words:
        output += w
        if output == s:
            return True
    return False

s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
sIsPrefix = isPrefixString(s,words)
print(sIsPrefix)
