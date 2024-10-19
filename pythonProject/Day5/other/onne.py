def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def is_special_number(num):

    digits = str(num)

    sum_of_factorials = sum(factorial(int(digit)) for digit in digits)

    return sum_of_factorials == num


user_input = int(input("Enter a number: "))

if is_special_number(user_input):
    print(f"{user_input} is a special number.")
else:
    print(f"{user_input} is not a special number.")
