
def decrypt(code, k):
    l = len(code)
    code = code + code
    if k > 0:
        for i in range(l):
            code[i] = sum(code[i+1:i+k+1])
        code = code[:l]
    elif k < 0:
        temp = code.copy()
        for i in range(l,l+l):
            code[i] = sum(temp[i+k:i])
        code = code[l:]
    else:
        code = [0] * l
    return code

code = [5,7,1,4]
k = 3
defuseCode = decrypt(code,k)
print(defuseCode)
