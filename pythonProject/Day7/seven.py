import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Address': ['123 Main St, CityA', '456 Park Ave, CityB', '789 Broadway, CityC'],
    'Age': [30, 25, 35]
}
dbda_df = pd.DataFrame(data)
dac_df = pd.DataFrame(data)
file_name = 'Vita.xlsx'

with pd.ExcelWriter(file_name) as writer:
    dbda_df.to_excel(writer, sheet_name='DBDA', index=False)
    dac_df.to_excel(writer, sheet_name='DAC', index=False)

print(f"{file_name} has been created successfully with sheets 'DBDA' and 'DAC'.")
