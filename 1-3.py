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

#A school play is being held over 2 nights. Tickets are $15 for adults and $10 for students. Design a program that inputs the number of adults and students who attended the play each night and displays the total amount of money collected and the profit made. Assume that the cost of the play was $9000.
adults = input("Enter the number of adults: ")
adults = int(adults)
students = input("Enter the number of students: ")
students = int(students)
total = adults*15 + students*10
profit = total - 9000
print("Total: " + str(total) + "\nProfit: " + str(profit))