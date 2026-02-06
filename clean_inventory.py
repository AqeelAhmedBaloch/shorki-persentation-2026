import pandas as pd

# Read Inventory sheet
excel_file = '2nd visit/2nd Visit Inventory.xlsx'
inventory_df = pd.read_excel(excel_file, sheet_name='Inventory ')

# Clean and prepare data - get only necessary columns
# Filter out rows with NaN in important columns
inventory_clean = inventory_df[['Unnamed: 1', 'Unnamed: 9']].dropna(subset=['Unnamed: 1'])
inventory_clean.columns = ['Item', 'Quantity']

# Remove header rows and clean
inventory_clean = inventory_clean[inventory_clean['Item'] != 'Description']
inventory_clean = inventory_clean[inventory_clean['Item'] != 'Vegetable Seeds']

# Reset index
inventory_clean = inventory_clean.reset_index(drop=True)

print("INVENTORY DATA:")
for idx, row in inventory_clean.iterrows():
    print(f"{idx+1}. {row['Item']} - Qty: {row['Quantity']}")

print(f"\nTotal: {len(inventory_clean)} items")
