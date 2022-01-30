def solution(number):
    number -= 1
    sum = 0
    while number > 0:
        if number % 3 == 0 or number % 5 == 0:
            sum += number
        number -= 1
    return sum

print(solution(10))
