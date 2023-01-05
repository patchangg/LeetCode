
def haveConflict(event1, event2):
    if event1[0] <= event2[1] and event2[0] <= event1[1]:
        return True
    else:
        return False

event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]
eventsConflict = haveConflict(event1,event2)
print(eventsConflict)
