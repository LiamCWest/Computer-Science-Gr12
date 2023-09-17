def inputInt(prompt):
    while(True):
        try: return int(input(prompt))
        except ValueError: pass

def askForFood():
    food = input("Enter a food: ")
    price = input("Enter the price of the food: ")
    return (tuple([food, price]))

items = inputInt("Enter the number of items: ")

foodDict = {}

for i in range(items):
    tup = askForFood()
    foodDict[tup[0]] = tup[1]

longest = 0

for i in foodDict:
    if(len(i)>longest): longest = len(i)

space = " "*int((longest-2)/2)
dash = "-"*(longest+10)
print(space + " Supermarket\n" + dash + "\nFood" + " "*(longest+1) + "Price\n" + dash)

mid1 = "   "

for i in foodDict:
    space = (longest+3-len(i))
    mid2 = " "*int(space)
    print(i + mid2 + "|" + mid1 +"$" + foodDict[i])


#calculate the sub total then tax then total
subtotal = 0
for i in foodDict:
    subtotal += float(foodDict[i])
print(dash)
print("Subtotal" + " "*(longest-3) + "$" + str(subtotal))
tax = subtotal*0.13
print("Tax" + " "*(longest+2) + "$" + str(tax))
total = subtotal + tax
print(dash + "\nTotal" + " "*(longest-1) + "$" + str(total))