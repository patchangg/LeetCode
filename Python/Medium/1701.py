
def averageWaitingTime(customers):
    wait = 0
    curr = 0
    for arrival, time in customers:
        curr = max(curr,arrival) + time
        wait += curr - arrival
    return wait / len(customers)

# Calculate the time the chef starts preparing the order and
# how long the customer had to wait for their order in each iteration. 
# Divide it by the how many customers came.
# O(n) where n is the amount of customers, O(1) space
customers = [[5,2],[5,4],[10,3],[20,1]]
averageWait = averageWaitingTime(customers)
pritn(averageWait)
