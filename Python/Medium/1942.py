import heapq

def smallestChair(times, targetFriend):
    occupied = list(range(0,len(times)))
    chair = [-1] * len(times)
    activity = []
    for idx, (arr,dep) in enumerate(times):
        activity.append((arr,True,idx))
        activity.append((dep,False,idx))
    heapq.heapify(activity)
    while activity:
        _, arrival, person = heapq.heappop(activity)
        if arrival:
            if person == targetFriend:
                return occupied[0]
            chair[person] = heapq.heappop(occupied)
        else:
            heapq.heappush(occupied, chair[person])

# Create a heap, storing the arrival/departure and index the person is in.
# Go through the heap, if it is an arrival, check if the person is the target
# friend, if so return the chair they are about to sit on otherwise
# assign the smallest unoccupied chair to the person. If it is a departure,
# remove the person from the occupied chair. O(n), O(n) space
times = [[1,4],[2,3],[4,6]]
targetFriend = 1
friendsChair = smallestChair(times,targetFriend)
print(friendsChair)
