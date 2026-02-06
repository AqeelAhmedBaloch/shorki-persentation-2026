import pandas as pd

excel_file = '2nd visit/2nd Visit Inventory.xlsx'

# Get all sheet names
xl = pd.ExcelFile(excel_file)
print("Available sheets:")
for i, sheet in enumerate(xl.sheet_names, 1):
    print(f"{i}. {sheet}")

# Read sheet 1 (first sheet)
sheet1_name = xl.sheet_names[0]
print(f"\n\nReading Sheet 1: {sheet1_name}")
df1 = pd.read_excel(excel_file, sheet_name=sheet1_name)
print(f"Rows: {len(df1)}, Columns: {len(df1.columns)}")
print("\nFirst 5 rows:")
print(df1.head().to_string())

# Read sheet 2 (second sheet)
sheet2_name = xl.sheet_names[1]
print(f"\n\nReading Sheet 2: {sheet2_name}")
df2 = pd.read_excel(excel_file, sheet_name=sheet2_name)
print(f"Rows: {len(df2)}, Columns: {len(df2.columns)}")
print("\nFirst 5 rows:")
print(df2.head().to_string())
