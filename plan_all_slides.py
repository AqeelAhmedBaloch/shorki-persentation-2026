import pandas as pd
import os

print("="*80)
print("GENERATING COMPLETE 2ND VISIT PRESENTATION")
print("="*80)

# ===== SLIDE 5: INVENTORY DATA =====
print("\n[1/3] Processing Inventory Data...")
file1 = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit\1. 2nd Visit Inventory.xlsx'
inventory_df = pd.read_excel(file1, sheet_name='Inventory ')

# Extract LEFT SIDE data (Items Purchased)
inventory_items = []
for idx in range(2, len(inventory_df)):
    desc = inventory_df.iloc[idx, 2]  # Description
    unit = inventory_df.iloc[idx, 3]  # Unit
    
    if pd.notna(desc) and str(desc).strip() != '':
        item_name = str(desc).strip()
        qty = str(int(unit)) if pd.notna(unit) and isinstance(unit, (int, float)) else str(unit) if pd.notna(unit) else 'Nill'
        
        inventory_items.append({
            'num': len(inventory_items) + 1,
            'name': item_name,
            'qty': qty
        })

print(f"   Inventory items: {len(inventory_items)}")

# ===== SLIDE 6: SEEDS DATA =====
print("\n[2/3] Processing Seeds Data...")
file2 = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit\2. 2nd sheet.xlsx'
seeds_df = pd.read_excel(file2, sheet_name='seeds')

seeds_items = []
for idx in range(2, len(seeds_df)):
    num = seeds_df.iloc[idx, 0]  # S.#
    desc = seeds_df.iloc[idx, 1]  # Description  
    measurement = seeds_df.iloc[idx, 2]  # Measurement
    
    if pd.notna(desc) and desc not in ['Description', 'Vegetable Seeds', 'Additional Seeds']:
        seeds_items.append({
            'num': int(num) if pd.notna(num) else len(seeds_items) + 1,
            'name': str(desc).strip(),
            'qty': str(measurement).strip() if pd.notna(measurement) else ''
        })

print(f"   Seeds items: {len(seeds_items)}")

# ===== SLIDES 7+: MEDIA FILES =====
print("\n[3/3] Processing Media Files...")
base_path = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit'

images = []
videos = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        ext = file.lower().split('.')[-1]
        rel_path = os.path.relpath(os.path.join(root, file), r'c:\Users\Aqeel\Desktop\shorkipresentation')
        rel_path = rel_path.replace('\\', '/')  # Convert to forward slashes for HTML
        
        if ext in ['jpg', 'jpeg', 'png']:
            images.append(rel_path)
        elif ext in ['mp4', 'mov', 'avi']:
            videos.append(rel_path)

print(f"   Images: {len(images)}")
print(f"   Videos: {len(videos)}")

# ===== CALCULATE SLIDES =====
print("\n" + "="*80)
print("SLIDE BREAKDOWN:")
print("="*80)

# Inventory: 2 columns, ~27 items each
inv_col1 = inventory_items[:27]
inv_col2 = inventory_items[27:]

# Seeds: 2 columns, ~16 items each  
seeds_col1 = seeds_items[:16]
seeds_col2 = seeds_items[16:]

# Images: 4 per slide
images_per_slide = 4
image_slides = []
for i in range(0, len(images), images_per_slide):
    image_slides.append(images[i:i+images_per_slide])

# Videos: 2 per slide
videos_per_slide = 2
video_slides = []
for i in range(0, len(videos), videos_per_slide):
    video_slides.append(videos[i:i+videos_per_slide])

print(f"Slide 4: 2nd Visit Title")
print(f"Slide 5: Inventory ({len(inventory_items)} items)")
print(f"Slide 6: Seeds ({len(seeds_items)} items)")
print(f"Slides 7-{6+len(image_slides)}: Images ({len(image_slides)} slides, {len(images)} total images)")
print(f"Slides {7+len(image_slides)}-{6+len(image_slides)+len(video_slides)}: Videos ({len(video_slides)} slides, {len(videos)} total videos)")
print(f"\nTotal 2nd Visit Slides: {3 + len(image_slides) + len(video_slides)}")
print(f"Grand Total Slides: {3 + 3 + len(image_slides) + len(video_slides)} (1st visit + 2nd visit)")

# Save summary
with open('presentation_summary.txt', 'w', encoding='utf-8') as f:
    f.write(f"PRESENTATION STRUCTURE\n")
    f.write(f"="*80 + "\n\n")
    f.write(f"1ST VISIT (Slides 1-3):\n")
    f.write(f"  - Slide 1: Title\n")
    f.write(f"  - Slide 2: Inventory\n")
    f.write(f"  - Slide 3: Pictures + Video\n\n")
    f.write(f"2ND VISIT (Slides 4-{6+len(image_slides)+len(video_slides)}):\n")
    f.write(f"  - Slide 4: Title\n")
    f.write(f"  - Slide 5: Inventory ({len(inventory_items)} items)\n")
    f.write(f"  - Slide 6: Seeds ({len(seeds_items)} items)\n")
    f.write(f"  - Slides 7-{6+len(image_slides)}: Images ({len(images)} total)\n")
    f.write(f"  - Slides {7+len(image_slides)}-{6+len(image_slides)+len(video_slides)}: Videos ({len(videos)} total)\n\n")
    f.write(f"TOTAL SLIDES: {3 + 3 + len(image_slides) + len(video_slides)}\n")

print("\nSummary saved to presentation_summary.txt")
print("Ready to generate HTML slides!")
