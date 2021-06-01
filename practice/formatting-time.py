#example for formatting time and date output 

from datetime import datetime

#times and dates can be formatted using a set of predefined string. 

def main():
    #the date and time at the current moment. 
    now = datetime.now()
    #place holder for date and time.
    print(now.strftime("The current year is: %Y"))
    #%y/%Y - year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("%a, %d, %B, %y"))

    #%c - locales date and time, %x - lacales date, %X - locales time
    print(now.strftime("locale date and time: %c"))
    print(now.strftime("locale date: %x"))
    print(now.strftime("locale time: %X"))

    #time formatting
    #%I/%H - 12/24 hour, %M - minute, %S - second, %p - loacles am/pm 
    print(now.strftime("current time: %I:%M:%S %p"))
    print(now.strftime("24 hourtime: %H:%M"))

if __name__ =="__main__":
    main()