from pandas import Series

values = []
for i in range(10):
    value = float(input(f"Enter value {i+1}: "))
    values.append(value)

data_series = Series(values)

print("\nThe entire Series:")
print(data_series)

third_element = data_series.iloc[2]
print(f"\nThe 3rd element is: {third_element}")

elements_4_to_7 = data_series.iloc[3:7]
print(f"\nElements from 4th to 7th are:\n{elements_4_to_7}")

fourth_last_to_last = data_series.iloc[-4:]
print(f"\nElements from the fourth last to the last are:\n{fourth_last_to_last}")

first_3_elements = data_series.iloc[:3]
print(f"\nThe first 3 elements are:\n{first_3_elements}")

fifth_position_element = data_series.iloc[4]
print(f"\nThe element at the 5th position is: {fifth_position_element}")
