day = (input("Enter the day the call started at:"))
time = float(input("Enter the time the call started at (hhmm):"))
minutes = float(input("Enter the duration of the call (in minutes):"))
if day == "mon" or \
        day == "tue" or \
        day == "wed" or \
        day == "thu" or \
        day == "fri" or \
        day == "Mon" or \
        day == "Tue" or \
        day == "Wed" or \
        day == "Thu" or \
        day == "Fri":
    weekday = 1
    if weekday == 1 and \
            800 <= time <= 1800:
        rate = 0.4
        output = rate * minutes
        output = "{:,.2f}".format(output)
        print("This call will cost $", output, sep="")

    else:
        rate = 0.25
        output = rate * minutes
        output = "{:,.2f}".format(output)
        print("This call will cost $", output, sep="")
# For Weekdays Saturday and Sunday
if day == "sat" or\
        day == "sun" or \
        day == "Sat" or \
        day == "Sun":
    rate = 0.15
    output = rate * minutes
    output = "{:,.2f}".format(output)
    print("This call will cost $", output, sep="")
