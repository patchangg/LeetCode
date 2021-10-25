class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overbooked = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overbooked:
            if start < j and end > i:
                return False
        for n, m in self.calendar:
            if start < m and end > n:
                self.overbooked.append((max(start,n),min(end,m)))
        self.calendar.append((start,end))
        return True

# Create a calendar and overbooked array which keeps track of double bookings
# For each new time entry, check if meets any overbooked time, if so that
# means it would be a triple booking so return False
# Next check if it would create a double booking, if so add it to the overbooked
# array, then add the time into the calendar and return true.
# book is O(n), and the calendar and overbooked array is O(n) space
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# Input
# ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, true, true, true, false, true, true]
