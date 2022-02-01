x = int(input("Enter Length of Race in Kilometers: "))
y = int(input("Enter Minutes: "))
z = int(input("Enter Seconds: "))
miles = x / 1.61
hour1 = y / 60
hour2 = z / 3600
print(miles / hour1 + hour2)