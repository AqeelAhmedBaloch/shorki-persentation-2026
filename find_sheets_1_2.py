import pandas as pd

excel_file = '2nd visit\\2nd Visit Inventory.xlsx'

# Get all sheet names
xl = pd.ExcelFile(excel_file)
print("Available sheets:")
for i, sheet in enumerate(xl.sheet_names, 1):
    print(f"{i}. {sheet}")

# Check if there are sheets named "1" and "2"
if '1' in xl.sheet_names and '2' in xl.sheet_names:
    print("\nFound sheets '1' and '2'!")
    
    # Read sheet 1
    print("\n" + "="*80)
    print("SHEET 1 DATA")
    print("="*80)
    df1 = pd.read_excel(excel_file, sheet_name='1')
    print(f"Rows: {len(df1)}, Columns: {len(df1.columns)}")
    print("\nFirst 10 rows:")
    print(df1.head(10).to_string())
    
    # Read sheet 2
    print("\n" + "="*80)
    print("SHEET 2 DATA")
    print("="*80)
    df2 = pd.read_excel(excel_file, sheet_name='2')
    print(f"Rows: {len(df2)}, Columns: {len(df2.columns)}")
    print("\nFirst 10 rows:")
    print(df2.head(10).to_string())
else:
    print("\nSheets '1' and '2' not found. Using first two sheets:")
    # Use first two sheets
    sheet1_name = xl.sheet_names[0]
    sheet2_name = xl.sheet_names[1]
    
    print(f"\nSheet 1: {sheet1_name}")
    df1 = pd.read_excel(excel_file, sheet_name=sheet1_name)
    print(f"Rows: {len(df1)}")
    
    print(f"\nSheet 2: {sheet2_name}")
    df2 = pd.read_excel(excel_file, sheet_name=sheet2_name)
    print(f"Rows: {len(df2)}")
