
def timeRequiredToBuy(tickets, k):
    output = 0
    for i in range(len(tickets)):
        if i <= k:
            output += min(tickets[i], tickets[k])
        else:
            output += min(tickets[i], tickets[k] - 1)
    return output

tickets = [2,3,2]
k = 2
timeToBuy = timeRequiredToBuy(tickets,k)
print(timeToBuy)
