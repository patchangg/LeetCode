accounts = [[1,2,3],[3,2,1]]
def maximumWealth(self, accounts):
    richest = 0
    for account in accounts:
        sum = 0
        for i in account:
            sum += i
        if sum > richest:
            richest = sum
    return richest

maximumWealth(self,accounts)
