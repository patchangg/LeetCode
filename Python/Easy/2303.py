
def calculateTax(brackets, income):
    output = 0
    prev = 0
    for u, p in brackets:
        if income >= u:
            output += (u - prev) * p / 100
            prev = u
        else:
            output += (income - prev) * p / 100
            return output
    return output

brackets = [[3,50],[7,10],[12,25]]
income = 10
taxOwed = calculateTax(brackets,income)
print(taxOwed)
