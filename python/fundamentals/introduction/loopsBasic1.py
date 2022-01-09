for x in range(0, 151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(0 ,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

total = 0
for x in range(1,500001,2):
    total += x
print(total)

for x in range(2018,0,-4):
    print(x)

bot = 2
top = 9
mult = 3
for x in range(bot,top + 1):
    if x % mult == 0:
        print(x)
