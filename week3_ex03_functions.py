def greet():
    print("Hello World!")
    greet()

def personalized_greeting(name):
    print(f"Hello {name}")
personalized_greeting("Raeesha")

def square(number):
    return number * number
result = square(5)
print(result)

def rectangle_area(length, width):
    return length * width
area = rectangle_area(4, 5)
print(area)

def apply_operation(func, number):
    return func(number)

def apply_operation(func, number):
    return func(number)

def double(number):
    return number * 2

print(apply_operation(double, 7))
print(apply_operation(square, 3))