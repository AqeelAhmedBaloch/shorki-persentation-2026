import pandas as pd

excel_file = '2nd visit/2nd Visit Inventory.xlsx'

# Read Inventory sheet
inventory_df = pd.read_excel(excel_file, sheet_name='Inventory ')

print("="*80)
print("COMPLETE INVENTORY SHEET ANALYSIS")
print("="*80)

# Show all column names
print("\nAll Columns:")
for i, col in enumerate(inventory_df.columns):
    print(f"  Column {i}: {col}")

print(f"\nTotal Rows in sheet: {len(inventory_df)}")

# Extract "In Store at Shorki" section (right side of sheet)
# Columns: 7 (Description), 8 (Unit), 9 (Rate per Unit)
print("\n" + "="*80)
print("IN STORE AT SHORKI - All Items")
print("="*80)

inventory_items = []
for idx in range(2, len(inventory_df)):  # Start from row 2 (after headers)
    desc = inventory_df.iloc[idx, 7]  # Column 8 - Description
    unit = inventory_df.iloc[idx, 8]  # Column 9 - Unit
    
    # Skip if description is NaN or empty
    if pd.notna(desc) and str(desc).strip() != '':
        item_name = str(desc).strip()
        
        # Format quantity
        if pd.notna(unit):
            if isinstance(unit, (int, float)):
                qty = str(int(unit)) if unit == int(unit) else str(unit)
            else:
                qty = str(unit).strip()
        else:
            qty = 'Nill'
        
        inventory_items.append({
            'num': len(inventory_items) + 1,
            'name': item_name,
            'qty': qty
        })

print(f"\nTotal Items Found: {len(inventory_items)}\n")

# Display all items
for item in inventory_items:
    print(f"{item['num']:2d}. {item['name']:<50s} | Qty: {item['qty']}")

# Save to file
with open('complete_inventory.txt', 'w', encoding='utf-8') as f:
    for item in inventory_items:
        f.write(f"{item['num']}|{item['name']}|{item['qty']}\n")

print(f"\n✓ Saved {len(inventory_items)} items to complete_inventory.txt")
