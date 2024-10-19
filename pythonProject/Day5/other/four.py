def calculate_simple_interest(principal, rate, years):
    return (principal * rate * years) / 100


try:
    principal_amount = float(input("Enter the principal amount: "))
    rate_of_interest = float(input("Enter the rate of interest (in %): "))
    number_of_years = float(input("Enter the number of years: "))

    simple_interest = calculate_simple_interest(principal_amount, rate_of_interest, number_of_years)


    print(f"The simple interest is: {simple_interest}")

except ValueError:
    print("Please enter valid numeric values.")
