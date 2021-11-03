
def letterCombinations(digits):
    if not digits:
        return []
    numpad = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
    output = []

    def dfs(digits,numpad,index,path):
        if len(path) == len(digits):
            output.append(path)
            return

        for j in numpad[digits[index]]:
            dfs(digits, numpad, index+1, path+j)

    dfs(digits,numpad,0,"")
    return output

# Create a dictionary containing the numpad letters.
# DFS each numpad letter, getting the different possible combinations for each
# numpad after itself in the digits. Once the combination is equal the the length
# of digits, that means that combination is done and append it a list.
# O(3^n) where n is the length of digits, O(1) space
digits = "23"
combinations = letterCombinations(digits)
print(combinations)
