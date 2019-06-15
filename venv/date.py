from datetime import date
from datetime import time
from datetime import datetime
def main():
    today=date.today()
    print("Today date is ", today)
    print('Today date is ', today)
    print('Date Components:', today.day, today.month, today.year)
    print('Date Components:', today.weekday())

    dat=datetime.now()
    print("The current date and time is", dat)
    print(dat.strftime("%Y"))
    print(dat.strftime("%Y-%m-%d"))

    t = datetime.time(datetime.now())
    print("The current date and time is", t)



main()


