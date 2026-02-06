import pandas as pd

# Read the Excel file
excel_file = '2nd visit/2nd Visit Inventory.xlsx'

print("="*60)
print("INVENTORY SHEET - Actual Data")
print("="*60)

# Read Inventory sheet
try:
    inventory_df = pd.read_excel(excel_file, sheet_name='Inventory ')
    
    # Display first few rows to understand structure
    print("\nFirst 10 rows:")
    print(inventory_df.head(10).to_string())
    
    print("\n\nColumn names:")
    print(inventory_df.columns.tolist())
    
    print(f"\n\nTotal rows: {len(inventory_df)}")
    
    # Try to find the actual data columns
    print("\n\nSample data from different columns:")
    for col in inventory_df.columns[:5]:
        print(f"\n{col}:")
        print(inventory_df[col].head(10).tolist())
        
except Exception as e:
    print(f"Error reading Inventory sheet: {e}")

print("\n" + "="*60)
print("SEEDS SHEET - Actual Data")
print("="*60)

# Read seeds sheet
try:
    seeds_df = pd.read_excel(excel_file, sheet_name='seeds')
    
    # Display first few rows
    print("\nFirst 10 rows:")
    print(seeds_df.head(10).to_string())
    
    print("\n\nColumn names:")
    print(seeds_df.columns.tolist())
    
    print(f"\n\nTotal rows: {len(seeds_df)}")
    
except Exception as e:
    print(f"Error reading Seeds sheet: {e}")
