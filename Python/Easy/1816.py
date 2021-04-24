
def truncateSentence(s, k):
    s = s.split(" ")
    i = 0
    String = []
    while i < k:
        String.append(s[i])
        i += 1
    return " ".join(String)


s = "Hello how are you Contestant"
k = 4
truncate = truncateSentence(s,k)
print(truncate)
