
def generateTheString(n):
    String = ""
    if (n % 2) == 0:
        n = n - 1
        for i in (range(n)):
            String += "a"
        String += "b"
    else:
        for i in range(n):
            String += "a"
    return String


n = 10
String = generateTheString(n)
print(String)
