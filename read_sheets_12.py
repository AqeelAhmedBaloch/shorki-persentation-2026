import pandas as pd
import os

# Check if file exists
file_path = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit\2nd Visit Inventory.xlsx'
print(f"Checking file: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")

if os.path.exists(file_path):
    # Get all sheet names
    xl = pd.ExcelFile(file_path)
    print(f"\nTotal sheets: {len(xl.sheet_names)}")
    print("\nAll sheet names:")
    for i, sheet in enumerate(xl.sheet_names, 1):
        print(f"{i}. '{sheet}'")
    
    # Check if there are sheets named "1" and "2"
    if '1' in xl.sheet_names and '2' in xl.sheet_names:
        print("\n✓ Found sheets '1' and '2'!")
        
        # Read sheet 1
        print("\n" + "="*80)
        print("SHEET '1' DATA")
        print("="*80)
        df1 = pd.read_excel(file_path, sheet_name='1')
        print(f"Rows: {len(df1)}, Columns: {len(df1.columns)}")
        print("\nFirst 5 rows:")
        print(df1.head().to_string())
        
        # Read sheet 2
        print("\n" + "="*80)
        print("SHEET '2' DATA")
        print("="*80)
        df2 = pd.read_excel(file_path, sheet_name='2')
        print(f"Rows: {len(df2)}, Columns: {len(df2.columns)}")
        print("\nFirst 5 rows:")
        print(df2.head().to_string())
    else:
        print("\nSheets '1' and '2' not found.")
        print("Please rename the sheets you want to use to '1' and '2'")
else:
    print("ERROR: File not found!")
