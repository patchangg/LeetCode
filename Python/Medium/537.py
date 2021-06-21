
def complexNumberMultiply(num1, num2):
    r1,i1 = num1.split('+')
    i1 = int(i1[:-1])
    r2,i2 = num2.split('+')
    i2 = int(i2[:-1])
    real = int(r1) * int(r2) - i1 * i2
    img = int(r1) * i2 + int(r2) * i1
    return '{}+{}i'.format(real,img)

# use the complex multiplication algorithm to find
# the multiplication of two complex numbers.
# O(n) time
num1 = "1+1i"
num2 = "1+1i"
complex = complexNumberMultiply(num1,num2)
print(complex)
