"""Doc."""


# Calculator v.2
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)
print(Back.GREEN)
print(Style.DIM)

what = input("What do You want to do? (+, -): ")

print(Back.CYAN)

a = float(input("Input 1-st component: "))
b = float(input("Input 2-d component: "))

print(Back.YELLOW)

if what == "+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c))
else:
    print("Invalid operation")

input()
