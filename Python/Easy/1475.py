
def finalPrices(prices):
    final = []
    length = len(prices)
    i = 0
    while i < length:
        j = i + 1
        final.append(prices[i])
        while j < length:
            if prices[j] <= prices[i]:
                final[i] = final[i] - prices[j]
                break
            j += 1
        i += 1
    return final


prices = [8,4,6,2,3]
final = finalPrices(prices)
print(final)
