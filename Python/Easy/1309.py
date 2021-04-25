
def freqAlphabets(s):
    dict = {}
    answer = ""
    for i in range(97,123):
        dict[i-96] = chr(i)
    if len(s) == 1:
        return dict[int(s[0])]
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == "#":
            answer += dict[int(s[i] + s[i + 1])]
            i += 3
        else:
            answer += dict[int(s[i])]
            i += 1
    return answer
    
s = "10#11#12"
map = freqAlphabets(s)
print(map)

#ascii a = 97, z = 122
