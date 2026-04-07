from datetime import datetime, time
import time

def current_data_time():
    print("=" * 30)
    print("Current data and time:",datetime.now())
    print("=" * 30)

def diffference_of_twodate():
    print("=" * 30)
    date1=input("Enter the first date(YYYY-MM-DD):")
    date2=input("Enter the second date(YYYY-MM-DD):")
    d1=datetime.strptime(date1,'%Y-%m-%d')
    d2=datetime.strptime(date2,'%Y-%m-%d')
    print("Difference:",abs((d1-d2).days))
    print("=" * 30)

def format_date():
    print("=" * 30)
    you_date=input("Enter the date(YYYY-MM-DD):")
    date=datetime.strptime(you_date,'%Y-%m-%d')
    custom_date=input("Enter the custom format like '%d-%m-%y':-")
    formatted_date=date.strftime(custom_date)
    print("Formatted date:",formatted_date)
    print("=" * 30)

def stopwatch():
    print("=" * 30)
    input("Press enter to start the stopwatch...")
    start_time=time.time()
    input("Press enter to stop the stopwatch...")
    end_time=time.time()
    diff=end_time-start_time
    print("Time elapsed:",diff)
    print("=" * 30)

def countdown():
    print("=" * 30)
    second=int(input("Enter the number of seconds:"))
    while second:
        time.sleep(1)
        second-=1
    print("time's up!")
    print("=" * 30)

def main():
    while True:
        print("=" * 30)
        print("Datetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        ch=int(input("Enter your choice:"))
        if (ch==1):
            current_data_time()
        elif(ch==2):
            diffference_of_twodate()
        elif(ch==3):
            format_date()
        elif(ch==4):
            stopwatch()
        elif(ch==5):
            countdown()
        elif(ch==6):
            break
        else:
            print("=" * 30)
            print("Invalid choice")
            print("=" * 30)

if __name__ == "__main__":
    main()