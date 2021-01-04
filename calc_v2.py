"""Doc."""


# Calculator v.2

what = input("What do You want to do? (+, -): ")
a = float(input("Input 1-st component: "))
b = float(input("Input 2-d component: "))

if what == "+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c))
else:
    print("Invalid operation")
