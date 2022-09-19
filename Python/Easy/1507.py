
def reformatDate(date):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    day,month,year = date.split(" ")
    if len(day) == 3:
        day = "0" + str(day[0])
    else:
        day = day[:2]
    if months.index(month) + 1 < 10:
        month = "0" + str(months.index(month) + 1)
    else:
        month = str(months.index(month) + 1)
    return year + "-" + month + "-" + day

date = "20th Oct 2052"
reformattedDate = reformatDate(date)
print(reformattedDate)
