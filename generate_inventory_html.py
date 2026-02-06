import pandas as pd

excel_file = '2nd visit/2nd Visit Inventory.xlsx'
inventory_df = pd.read_excel(excel_file, sheet_name='Inventory ')

print("Extracting LEFT SIDE: ITEMS PURCHASE FOR SHORKI")
print("="*80)

# LEFT SIDE: Columns 1 (S.#), 2 (Description), 3 (Unit)
items = []
for idx in range(2, len(inventory_df)):
    s_no = inventory_df.iloc[idx, 1]  # S.#
    desc = inventory_df.iloc[idx, 2]  # Description
    unit = inventory_df.iloc[idx, 3]  # Unit
    
    # Skip empty rows
    if pd.notna(desc) and str(desc).strip() != '':
        item_name = str(desc).strip()
        
        # Format unit/quantity
        if pd.notna(unit):
            if isinstance(unit, (int, float)):
                qty = str(int(unit)) if unit == int(unit) else str(unit)
            else:
                qty = str(unit).strip()
        else:
            qty = 'Nill'
        
        items.append({
            'num': len(items) + 1,
            'name': item_name,
            'qty': qty
        })

print(f"Total items extracted: {len(items)}\n")

# Display first 10
for i, item in enumerate(items[:10], 1):
    print(f"{i:2d}. {item['name']:<50s} | {item['qty']}")

# Split into two columns for display (26-27 items each)
mid_point = (len(items) + 1) // 2

col1_items = items[:mid_point]
col2_items = items[mid_point:]

print(f"\nColumn 1: {len(col1_items)} items")
print(f"Column 2: {len(col2_items)} items")

# Generate HTML for both columns
html_output = ""

# Column 1
html_output += "<!-- Column 1 -->\n"
html_output += '<div class="inventory-column">\n'
html_output += '    <table class="inventory-table">\n'
html_output += '        <thead><tr><th>#</th><th>Item Name</th><th>Qty</th></tr></thead>\n'
html_output += '        <tbody>\n'

for item in col1_items:
    html_output += f'            <tr><td>{item["num"]}</td><td>{item["name"]}</td><td>{item["qty"]}</td></tr>\n'

html_output += '        </tbody>\n'
html_output += '    </table>\n'
html_output += '</div>\n\n'

# Column 2
html_output += "<!-- Column 2 -->\n"
html_output += '<div class="inventory-column">\n'
html_output += '    <table class="inventory-table">\n'
html_output += '        <thead><tr><th>#</th><th>Item Name</th><th>Qty</th></tr></thead>\n'
html_output += '        <tbody>\n'

for item in col2_items:
    html_output += f'            <tr><td>{item["num"]}</td><td>{item["name"]}</td><td>{item["qty"]}</td></tr>\n'

html_output += '        </tbody>\n'
html_output += '    </table>\n'
html_output += '</div>\n'

# Save HTML
with open('inventory_slide_html.txt', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("\nHTML generated and saved to inventory_slide_html.txt")
print(f"Ready to update Slide 5 with {len(items)} items!")
