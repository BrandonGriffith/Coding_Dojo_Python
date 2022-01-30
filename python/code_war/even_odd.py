def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"




print(even_or_odd(12))

def square_digits(num):
    numm = str(num)
    x = ""
    z = 0
    for i in numm:
        x = x + str(int(numm[z]) ** 2)
        z = z + 1
    return int(x)

print(square_digits(1234))

def square_digits2(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

print(square_digits2(1234))
