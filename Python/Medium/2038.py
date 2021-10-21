
def winnerOfGame(colors):
    alice = 0
    bob = 0
    for i in range(1,len(colors)-1):
        if colors[i-1] == colors[i] == colors[i+1]:
            if colors[i] == "A":
                alice += 1
            else:
                bob += 1
    return alice>bob

# Count how many AAA or BBB substrings are in the string to get how many
# times Alice or Bob can take a letter out of the string
# Alice has to have greater amount of points than bob as she starts first to win
# O(n),O(1) space
colors = "AAABABB"
doesAliceWin = winnerOfGame(colors)
print(doesAliceWin)
