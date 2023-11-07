import math

seconds = input("Enter the number of seconds: ")
seconds = int(seconds)
hours = int(seconds/3600)
seconds = seconds%3600
minutes = int(seconds/60)
seconds = seconds%60
print("Hours: " + str(hours) + "\nMinutes: " + str(minutes) + "\nSeconds: " + str(seconds))

interestRate = input("Enter the interest rate: ")
interestRate = float(interestRate)
final = input("Enter the final amount: ")
final = float(final)
years = input("Enter the number of years: ")
years = int(years)
initial = final/(1+interestRate)**years
print("Initial amount: " + str(initial))

adults = input("Enter the number of adults: ")
adults = int(adults)
students = input("Enter the number of students: ")
students = int(students)
total = adults*15 + students*10
profit = total - 9000
print("Total: " + str(total) + "\nProfit: " + str(profit))

a = input("Enter a: ")
a = float(a)
b = input("Enter b: ")
b = float(b)
c = input("Enter c: ")
c = float(c)
x = -b/(2*a)
y = a*x**2 + b*x + c
print("Vertex: (" + str(x) + ", " + str(y) + ")")
if a > 0:
    print("Parabola is open upward")
elif a < 0:
    print("Parabola is open downward")
else:
    print("Parabola is a line")
if y > 0:
    print("Parabola is above the x-axis")
elif y < 0:
    print("Parabola is below the x-axis")
else:
    print("Parabola is on the x-axis")
if b**2 - 4*a*c > 0:
    print("Parabola cuts the x-axis at (" + str((-b + (b**2 - 4*a*c)**0.5)/(2*a)) + ", 0) and (" + str((-b - (b**2 - 4*a*c)**0.5)/(2*a)) + ", 0)")
elif b**2 - 4*a*c == 0:
    print("Parabola cuts the x-axis at (" + str(-b/(2*a)) + ", 0)")
else:
    print("Parabola does not cut the x-axis")

x1 = input("Enter x1: ")
x1 = float(x1)
y1 = input("Enter y1: ")
y1 = float(y1)
x2 = input("Enter x2: ")
x2 = float(x2)
y2 = input("Enter y2: ")
y2 = float(y2)
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print("Distance: " + str(distance))
if x1 == x2:
    print("Equation of line: x = " + str(x1))
elif y1 == y2:
    print("Equation of line: y = " + str(y1))
else:
    slope = (y1 - y2)/(x1 - x2)
    intercept = y1 - slope*x1
    print("Equation of line: y = " + str(slope) + "x + " + str(intercept))

print("Angle: " + str(180 - 90 - 180*math.Tan(8.2/9.6)/math.Pi) + " degrees")