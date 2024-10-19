def is_armstrong(number):

    digits = str(number)
    power = len(digits)
    sum_of_powers = sum(int(digit) ** power for digit in digits)

    return sum_of_powers == number

print("4-digit Armstrong numbers:")
for num in range(1000, 10000):
    if is_armstrong(num):
        print(num)
