
def average(salary):
    salary.sort()
    length = len(salary)
    average = 0
    counter = 0
    for num in range(1,length-1):
        counter += 1
        average += salary[num]
    return (average/counter)


salary = [8000,9000,2000,3000,6000,1000]
middle = average(salary)
print(middle)
