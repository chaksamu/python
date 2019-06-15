import calendar

for month in calendar.month_name:
 print(month)
for month in calendar.day_name:
 print(month)
for month in calendar.day_name:
 print(month)

 c=calendar.TextCalendar(calendar.SUNDAY)
 str=c.formatmonth(2025,12)
 print(str)

 c = calendar.TextCalendar(calendar.TUESDAY)
 str = c.formatmonth(2025, 2)
 print(str)


 c = calendar.HTMLCalendar(calendar.TUESDAY)
 str = c.formatmonth(2025, 2)
 print(str)

 c = calendar.TextCalendar(calendar.TUESDAY)
 for i in c.itermonthdays(2025,4):
  print(i)

 for month in range (1,13):
  mycal=calendar.monthcalendar(2025,month)
  print(mycal)