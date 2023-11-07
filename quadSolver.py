import cmath

def inputFloat(prompt):
    while(True):
        try: return float(input(prompt))
        except ValueError: pass

a = inputFloat("Enter a: ")
b = inputFloat("Enter b: ")
c = inputFloat("Enter c: ")

d = (b*b) - (4*a*c)

roots = ("two" if d > 0 else "one" if d == 0 else "complex")

print("The discriminant is {}.\nThere are {} solutions to {}x^2 + {}x + {}.".format(d, roots, a, b, c))

if d > 0:
    x1 = (-b + cmath.sqrt(d)) / (2*a)
    x2 = (-b - cmath.sqrt(d)) / (2*a)
    print("The solutions are {} and {}.".format(x1, x2))
elif d == 0:
    x = -b / (2*a)
    print("The solution is {}.".format(x))
else:
    x1 = (-b + cmath.sqrt(d)) / (2*a)
    x2 = (-b - cmath.sqrt(d)) / (2*a)
    print("The solutions are {} and {}.".format(x1, x2))