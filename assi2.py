
x=("Hello, world!")
print(x)

a = 10
b = 20
print(a + b)
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
import math
print(math.pi)
PI = 3.14
print(PI)
num = 5
square = num * num
print(square)
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("Area of the circle is:", area)
x = 5
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

z = "Hello, World!"
print(type(z))  # <class 'str'>
import math

# Square root
print(math.sqrt(16))  # 4.0

# Power (x raised to y)
print(math.pow(2, 3))  # 8.0

# Pi value
print(math.pi)  # 3.141592653589793

# Trigonometric functions
angle = 90
# Converting angle to radians first
radians = math.radians(angle)
print(math.sin(radians))  # 1.0 (sine of 90 degrees)

# Logarithmic functions
print(math.log(100, 10))  # 2.0 (log base 10 of 100)

# Factorial
print(math.factorial(5))  # 120 (5! = 5*4*3*2*1)

# Absolute value
print(math.fabs(-7))  # 7.0 (absolute value)
a = 5
b = 5
result = a ** b
print(result)
