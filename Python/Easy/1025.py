
def divisorGame(n):
    return n % 2 == 0

n = 4
winner = divisorGame(n)
print(n)
# n % 2 == 0 works as ALice only ever wins when the number is even
# as a odd number is impossible to win when going first
# as they will make sure that the number is always odd 
