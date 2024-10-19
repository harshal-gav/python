def sum_of_digits(number):

    return sum(int(digit) for digit in str(number))

user_input = input("Enter a number (maximum 5 digits): ")


if user_input.isdigit() and len(user_input) <= 5:
    number = int(user_input)
    digit_sum = sum_of_digits(number)
    print(f"The sum of the digits of {number} is: {digit_sum}")
else:
    print("Please enter a valid 5-digit number.")
