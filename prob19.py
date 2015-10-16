weekday = 1
day = 1
mon = 1
year = 1900
count = 0
while(year < 2001):
	if((year >= 1901) and (year <= 2000) and (weekday == 0) and (day == 1)):
		print(str(year) + ":" + str(mon) + ":" + str(day) + ":" + str(weekday))
		count = count + 1
	weekday = (weekday + 1) % 7
	if((mon == 9) or (mon == 4) or (mon == 6) or (mon == 11)):	
		if(day + 1 > 30):
			day = 1
			mon = mon + 1
		else:
			day = day + 1
	elif(mon == 2):
		schaltjahr = (year != 1900) and (year % 4 == 0)
		if(schaltjahr and day + 1 > 29):
			day = 1
			mon = mon + 1
		elif(day + 1 > 28):
			day = 1
			mon = mon + 1
		else:
			day = day + 1
	elif(mon == 12):
		if(day + 1 > 31):
			day = 1
			mon = 1
			year = year + 1
		else:
			day = day + 1
	else:
		if(day + 1 > 31):
			day = 1
			mon = mon + 1
		else:
			day = day + 1
print(count)
