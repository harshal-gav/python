import pandas as pd

values = []

for i in range(5):
    value = float(input(f"Enter value {i+1}: "))
    values.append(value)

data_series = pd.Series(values)

series_sum = data_series.sum()
print(f"\nThe sum of the Series is: {series_sum}")

value_to_add = float(input("Enter a value to add: "))
result_add = data_series + value_to_add
print(f"\nSeries after adding {value_to_add}:\n{result_add}")

value_to_subtract = float(input("Enter a value to subtract: "))
result_subtract = data_series - value_to_subtract
print(f"\nSeries after subtracting {value_to_subtract}:\n{result_subtract}")

value_to_multiply = float(input("Enter a value to multiply: "))
result_multiply = data_series * value_to_multiply
print(f"\nSeries after multiplying by {value_to_multiply}:\n{result_multiply}")

value_to_add_again = float(input("Enter another value to add: "))
result_add_again = data_series + value_to_add_again
print(f"\nSeries after adding {value_to_add_again}:\n{result_add_again}")
