import pandas as pd

# File 1: For Slide 5
file1 = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit\1. 2nd Visit Inventory.xlsx'
print("="*80)
print("FILE 1: For Slide 5")
print("="*80)

xl1 = pd.ExcelFile(file1)
print(f"Sheets in File 1: {xl1.sheet_names}")

# Read first sheet
df1 = pd.read_excel(file1, sheet_name=xl1.sheet_names[0])
print(f"\nSheet: {xl1.sheet_names[0]}")
print(f"Rows: {len(df1)}, Columns: {len(df1.columns)}")
print("\nFirst 5 rows:")
print(df1.head().to_string())

# File 2: For Slide 6
file2 = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit\2. 2nd sheet.xlsx'
print("\n" + "="*80)
print("FILE 2: For Slide 6")
print("="*80)

xl2 = pd.ExcelFile(file2)
print(f"Sheets in File 2: {xl2.sheet_names}")

# Read first sheet
df2 = pd.read_excel(file2, sheet_name=xl2.sheet_names[0])
print(f"\nSheet: {xl2.sheet_names[0]}")
print(f"Rows: {len(df2)}, Columns: {len(df2.columns)}")
print("\nFirst 5 rows:")
print(df2.head().to_string())
