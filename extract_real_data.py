import pandas as pd

excel_file = '2nd visit/2nd Visit Inventory.xlsx'

# Read Inventory sheet - "In Store at Shorki" section
inventory_df = pd.read_excel(excel_file, sheet_name='Inventory ')

# Extract "In Store at Shorki" data (columns 7, 8, 9)
# Row 1 has headers, data starts from row 2
inventory_items = []
for idx in range(2, len(inventory_df)):
    desc = inventory_df.iloc[idx, 7]  # Column 8 (Unnamed: 7) - Description
    unit = inventory_df.iloc[idx, 8]  # Column 9 (Unnamed: 8) - Unit
    
    if pd.notna(desc) and desc != 'Description':
        inventory_items.append({
            'num': len(inventory_items) + 1,
            'name': str(desc).strip(),
            'qty': str(int(unit)) if pd.notna(unit) and isinstance(unit, (int, float)) else str(unit) if pd.notna(unit) else ''
        })

print("INVENTORY ITEMS (In Store at Shorki):")
print(f"Total: {len(inventory_items)}")
for item in inventory_items[:5]:
    print(f"{item['num']}. {item['name']} - {item['qty']}")

# Read Seeds sheet
seeds_df = pd.read_excel(excel_file, sheet_name='seeds')

# Extract seeds data
seeds_items = []
for idx in range(2, len(seeds_df)):
    num = seeds_df.iloc[idx, 0]  # Column 1 (Unnamed: 0) - S.#
    desc = seeds_df.iloc[idx, 1]  # Column 2 (Unnamed: 1) - Description  
    measurement = seeds_df.iloc[idx, 2]  # Column 3 (Unnamed: 2) - Measurement
    
    if pd.notna(desc) and desc not in ['Description', 'Vegetable Seeds', 'Additional Seeds']:
        seeds_items.append({
            'num': int(num) if pd.notna(num) else len(seeds_items) + 1,
            'name': str(desc).strip(),
            'qty': str(measurement).strip() if pd.notna(measurement) else ''
        })

print(f"\nSEEDS ITEMS:")
print(f"Total: {len(seeds_items)}")
for item in seeds_items[:5]:
    print(f"{item['num']}. {item['name']} - {item['qty']}")

# Save to file for HTML generation
with open('inventory_data.txt', 'w', encoding='utf-8') as f:
    f.write("INVENTORY:\n")
    for item in inventory_items:
        f.write(f"{item['num']}|{item['name']}|{item['qty']}\n")
    
    f.write("\nSEEDS:\n")
    for item in seeds_items:
        f.write(f"{item['num']}|{item['name']}|{item['qty']}\n")

print("\n✓ Data saved to inventory_data.txt")
