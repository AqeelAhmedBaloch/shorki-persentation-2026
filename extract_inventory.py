import pandas as pd
import json

file_path = r'c:\Users\Aqeel\Desktop\shorkipresentation\1st Visit\1st visit.xlsx'

try:
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Clean up the data - remove rows where all values are NaN
    df = df.dropna(how='all')
    
    # Get the relevant columns (assuming structure from previous output)
    # The data appears to be in columns with item numbers, names, and quantities
    
    # Extract meaningful data
    inventory = []
    for index, row in df.iterrows():
        # Skip header rows and empty rows
        if pd.notna(row.iloc[3]) and pd.notna(row.iloc[4]):
            try:
                item_no = int(row.iloc[3]) if pd.notna(row.iloc[3]) else None
                item_name = str(row.iloc[4]) if pd.notna(row.iloc[4]) else ""
                quantity = int(row.iloc[5]) if pd.notna(row.iloc[5]) else 0
                
                if item_no and item_name:
                    inventory.append({
                        "no": item_no,
                        "name": item_name.strip(),
                        "quantity": quantity
                    })
            except:
                continue
    
    # Output as JSON
    print(json.dumps(inventory, indent=2, ensure_ascii=False))
    
except Exception as e:
    print(f"Error: {e}")
