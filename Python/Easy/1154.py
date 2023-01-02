
def dayOfYear(date):
	days = [31,28,31,30,31,30,31,31,30,31,30,31]
	year,month,day = date.split("-")
	if (int(year) % 400 == 0) and (int(year) % 100 == 0):
		days[1] = 29
	elif (int(year) % 4 == 0) and (int(year) % 100 != 0):
		days[1] = 29
	output = 0
	for i in range(int(month)):
		if i == int(month) - 1:
			output += int(day)
		else:
			output += days[i]
	return output

date = "2019-01-09"
daysOfTheYear = dayOfYear(date)
print(daysOfTheYear)
