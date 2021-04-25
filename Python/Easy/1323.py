
def maximum69Number(num):
    String = list(str(num))
    maximum = num
    for i in range(len(String)):
        temps = String.copy()
        if temps[i] == "6":
            temps[i] = "9"
        elif temps[i] == "9":
            temps[i] = "6"
        number = "".join(temps)
        if int(number) > maximum:
            maximum = int(number)
    return maximum

num = 9996
max = maximum69Number(num)
print(max)
