
def intToRoman(num):
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    output = ""
    for i,val in enumerate(nums):
        output += (num//val) * numerals[i]
        num %= val
    return output

# Constraint is 3999 so the highest numeral we will use is M
# Loop through the numbers, removing it from num and adding numeral to the output
# O(13), O(1) space
num = 3
roman = intToRoman(num)
print(roman)
