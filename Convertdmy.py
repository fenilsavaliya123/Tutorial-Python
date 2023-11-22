#Convert Dmy
a=int(input("Enter Sceound:"))

year=a/365
year=int(year)
week=(a%365)/7
week=int(week)
day=(a%365)%7
day=int(day)




print("***year:",year,"***Week:",week,"***day:",day)

