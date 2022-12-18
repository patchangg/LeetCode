
def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

x = 121
isXAPalindrome = isPalindrome(x)
print(isXAPalindrome)
