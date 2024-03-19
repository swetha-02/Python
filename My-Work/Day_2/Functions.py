#Positional Arguments

def week(days,month):
    print(f"Today is 4th {days} of {month}")
week("Thursday", "August")

#Keyword Arguments

week(month="August",days="Saturday")

#Default Arguments

def week(days="Saturday",month="August"):
    print(f"Today is 4th {days} of {month}")
week()