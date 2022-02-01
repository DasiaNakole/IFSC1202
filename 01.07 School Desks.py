a = int(input("Enter Classroom A: "))
b = int(input("Enter Classroom B: "))
c = int(input("Enter Classroom C: "))
d = a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2
print(d)