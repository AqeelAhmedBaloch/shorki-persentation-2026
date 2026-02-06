import pandas as pd

# Read the Excel file
excel_file = '2nd visit/2nd Visit Inventory.xlsx'

# Read Inventory sheet
inventory_df = pd.read_excel(excel_file, sheet_name='Inventory ')
print("=== INVENTORY SHEET ===")
print(inventory_df.to_string(index=False))
print(f"\nTotal rows: {len(inventory_df)}")

print("\n" + "="*50 + "\n")

# Read seeds sheet
seeds_df = pd.read_excel(excel_file, sheet_name='seeds')
print("=== SEEDS SHEET ===")
print(seeds_df.to_string(index=False))
print(f"\nTotal rows: {len(seeds_df)}")
