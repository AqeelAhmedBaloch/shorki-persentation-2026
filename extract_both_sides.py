import pandas as pd

excel_file = '2nd visit/2nd Visit Inventory.xlsx'
inventory_df = pd.read_excel(excel_file, sheet_name='Inventory ')

print("="*80)
print("LEFT SIDE: ITEMS PURCHASED")
print("="*80)

# Left side: Columns 1 (S.#), 2 (Description), 3 (Unit)
left_items = []
for idx in range(2, len(inventory_df)):
    s_no = inventory_df.iloc[idx, 1]  # Column 2 - S.#
    desc = inventory_df.iloc[idx, 2]  # Column 3 - Description
    unit = inventory_df.iloc[idx, 3]  # Column 4 - Unit
    
    if pd.notna(desc) and str(desc).strip() != '':
        item_name = str(desc).strip()
        
        if pd.notna(unit):
            if isinstance(unit, (int, float)):
                qty = str(int(unit)) if unit == int(unit) else str(unit)
            else:
                qty = str(unit).strip()
        else:
            qty = ''
        
        left_items.append({
            'num': len(left_items) + 1,
            'name': item_name,
            'qty': qty
        })

print(f"Total Items (Left): {len(left_items)}\n")
for item in left_items[:10]:
    print(f"{item['num']:2d}. {item['name']:<45s} | Qty: {item['qty']}")

print("\n" + "="*80)
print("RIGHT SIDE: IN STORE AT SHORKI")
print("="*80)

# Right side: Columns 7 (Description), 8 (Unit)
right_items = []
for idx in range(2, len(inventory_df)):
    desc = inventory_df.iloc[idx, 7]  # Column 8 - Description
    unit = inventory_df.iloc[idx, 8]  # Column 9 - Unit
    
    if pd.notna(desc) and str(desc).strip() != '':
        item_name = str(desc).strip()
        
        if pd.notna(unit):
            if isinstance(unit, (int, float)):
                qty = str(int(unit)) if unit == int(unit) else str(unit)
            else:
                qty = str(unit).strip()
        else:
            qty = 'Nill'
        
        right_items.append({
            'num': len(right_items) + 1,
            'name': item_name,
            'qty': qty
        })

print(f"Total Items (Right): {len(right_items)}\n")
for item in right_items[:10]:
    print(f"{item['num']:2d}. {item['name']:<45s} | Qty: {item['qty']}")

print("\n" + "="*80)
print(f"TOTAL INVENTORY ITEMS: {len(left_items)} + {len(right_items)} = {len(left_items) + len(right_items)}")
print("="*80)

# Save combined data
with open('all_inventory_items.txt', 'w', encoding='utf-8') as f:
    f.write("LEFT_SIDE:\n")
    for item in left_items:
        f.write(f"{item['num']}|{item['name']}|{item['qty']}\n")
    
    f.write("\nRIGHT_SIDE:\n")
    for item in right_items:
        f.write(f"{item['num']}|{item['name']}|{item['qty']}\n")

print("\nData saved to all_inventory_items.txt")
