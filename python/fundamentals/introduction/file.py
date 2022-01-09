num1 = 42   # variable declaration
num2 = 2.3  # variable declaration
boolean = True  # variable declaration
string = 'Hello World'  # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # variable declaration
fruit = ('blueberry', 'strawberry', 'banana')   # variable declaration
print(type(fruit))  # type check
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

if num1 > 45:   # conditional
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: # conditional
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):      # for loop
    print(x)
for x in range(2,5):    # for loop
    print(x)
for x in range(2,10,3): # for loop
    print(x)
x = 0
while(x < 5):           # while loop
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:      # for loop
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():    # function
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):     # function
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):     # function
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
