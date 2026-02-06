import pandas as pd
import json

file_path = r'c:\Users\Aqeel\Desktop\shorkipresentation\1st Visit\1st visit.xlsx'

try:
    # Read all sheets
    xls = pd.ExcelFile(file_path)
    data = {}
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        data[sheet_name] = df.to_dict(orient='records')
    
    print(json.dumps(data, indent=2))
except Exception as e:
    print(f"Error: {e}")
