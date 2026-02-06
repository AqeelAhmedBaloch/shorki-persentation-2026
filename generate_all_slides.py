import pandas as pd
import os

# Read data
file1 = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit\1. 2nd Visit Inventory.xlsx'
file2 = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit\2. 2nd sheet.xlsx'

inventory_df = pd.read_excel(file1, sheet_name='Inventory ')
seeds_df = pd.read_excel(file2, sheet_name='seeds')

# Extract inventory
inventory_items = []
for idx in range(2, len(inventory_df)):
    desc = inventory_df.iloc[idx, 2]
    unit = inventory_df.iloc[idx, 3]
    if pd.notna(desc) and str(desc).strip() != '':
        inventory_items.append({
            'num': len(inventory_items) + 1,
            'name': str(desc).strip(),
            'qty': str(int(unit)) if pd.notna(unit) and isinstance(unit, (int, float)) else str(unit) if pd.notna(unit) else 'Nill'
        })

# Extract seeds
seeds_items = []
for idx in range(2, len(seeds_df)):
    num = seeds_df.iloc[idx, 0]
    desc = seeds_df.iloc[idx, 1]
    measurement = seeds_df.iloc[idx, 2]
    if pd.notna(desc) and desc not in ['Description', 'Vegetable Seeds', 'Additional Seeds']:
        seeds_items.append({
            'num': int(num) if pd.notna(num) else len(seeds_items) + 1,
            'name': str(desc).strip(),
            'qty': str(measurement).strip() if pd.notna(measurement) else ''
        })

# Get media files
base_path = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit'
images = []
videos = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        ext = file.lower().split('.')[-1]
        rel_path = os.path.relpath(os.path.join(root, file), r'c:\Users\Aqeel\Desktop\shorkipresentation')
        rel_path = rel_path.replace('\\', '/')
        
        if ext in ['jpg', 'jpeg', 'png']:
            images.append(rel_path)
        elif ext in ['mp4', 'mov', 'avi']:
            videos.append(rel_path)

# Generate complete HTML
html = ""
slide_num = 4

# ===== SLIDE 4: TITLE =====
html += f'''
<!-- Slide {slide_num}: 2nd Visit Shorki Title -->
<section class="slide" data-slide="{slide_num}">
    <div class="slide-content">
        <div class="title-wrapper">
            <h1 class="main-title">2nd Visit Shorki</h1>
            <div class="subtitle">Agricultural Products & Seeds Overview</div>
            <div class="date-badge">January 2026</div>
        </div>
        <div class="decorative-element"></div>
    </div>
</section>

'''
slide_num += 1

# ===== SLIDE 5: INVENTORY =====
mid = (len(inventory_items) + 1) // 2
inv_col1 = inventory_items[:mid]
inv_col2 = inventory_items[mid:]

html += f'''<!-- Slide {slide_num}: Inventory -->
<section class="slide" data-slide="{slide_num}">
    <div class="slide-content">
        <h2 class="slide-title">Inventory</h2>
        <div class="inventory-grid">
            <!-- Column 1 -->
            <div class="inventory-column">
                <table class="inventory-table">
                    <thead><tr><th>#</th><th>Item Name</th><th>Qty</th></tr></thead>
                    <tbody>
'''

for item in inv_col1:
    html += f'                        <tr><td>{item["num"]}</td><td>{item["name"]}</td><td>{item["qty"]}</td></tr>\n'

html += '''                    </tbody>
                </table>
            </div>

            <!-- Column 2 -->
            <div class="inventory-column">
                <table class="inventory-table">
                    <thead><tr><th>#</th><th>Item Name</th><th>Qty</th></tr></thead>
                    <tbody>
'''

for item in inv_col2:
    html += f'                        <tr><td>{item["num"]}</td><td>{item["name"]}</td><td>{item["qty"]}</td></tr>\n'

html += '''                    </tbody>
                </table>
            </div>
        </div>
    </div>
</section>

'''
slide_num += 1

# ===== SLIDE 6: SEEDS =====
mid = (len(seeds_items) + 1) // 2
seeds_col1 = seeds_items[:mid]
seeds_col2 = seeds_items[mid:]

html += f'''<!-- Slide {slide_num}: Seeds -->
<section class="slide" data-slide="{slide_num}">
    <div class="slide-content">
        <h2 class="slide-title">Seeds Inventory</h2>
        <div class="inventory-grid">
            <!-- Column 1 -->
            <div class="inventory-column">
                <table class="inventory-table">
                    <thead><tr><th>#</th><th>Seed Name</th><th>Qty</th></tr></thead>
                    <tbody>
'''

for item in seeds_col1:
    html += f'                        <tr><td>{item["num"]}</td><td>{item["name"]}</td><td>{item["qty"]}</td></tr>\n'

html += '''                    </tbody>
                </table>
            </div>

            <!-- Column 2 -->
            <div class="inventory-column">
                <table class="inventory-table">
                    <thead><tr><th>#</th><th>Seed Name</th><th>Qty</th></tr></thead>
                    <tbody>
'''

for item in seeds_col2:
    html += f'                        <tr><td>{item["num"]}</td><td>{item["name"]}</td><td>{item["qty"]}</td></tr>\n'

html += '''                    </tbody>
                </table>
            </div>
        </div>
    </div>
</section>

'''
slide_num += 1

# ===== IMAGE SLIDES (4 per slide) =====
images_per_slide = 4
for i in range(0, len(images), images_per_slide):
    batch = images[i:i+images_per_slide]
    
    html += f'''<!-- Slide {slide_num}: Images {i+1}-{min(i+images_per_slide, len(images))} -->
<section class="slide" data-slide="{slide_num}">
    <div class="slide-content">
        <h2 class="slide-title">2nd Visit Gallery - Part {(i//images_per_slide)+1}</h2>
        <div class="images-grid-large">
'''
    
    for img in batch:
        filename = os.path.basename(img)
        caption = filename.replace('.jpeg', '').replace('.jpg', '').replace('WhatsApp Image ', '').replace(' at ', ' ')
        html += f'''            <div class="gallery-item-large" onclick="zoomImage(this)">
                <img src="{img}" alt="{caption}">
                <div class="gallery-caption">{caption}</div>
            </div>
'''
    
    html += '''        </div>
    </div>
</section>

'''
    slide_num += 1

# ===== VIDEO SLIDES (2 per slide) =====
videos_per_slide = 2
for i in range(0, len(videos), videos_per_slide):
    batch = videos[i:i+videos_per_slide]
    
    html += f'''<!-- Slide {slide_num}: Videos {i+1}-{min(i+videos_per_slide, len(videos))} -->
<section class="slide" data-slide="{slide_num}">
    <div class="slide-content">
        <h2 class="slide-title">2nd Visit Videos - Part {(i//videos_per_slide)+1}</h2>
        <div class="videos-grid">
'''
    
    for vid_idx, vid in enumerate(batch):
        filename = os.path.basename(vid)
        caption = filename.replace('.mp4', '').replace('WhatsApp Video ', '').replace(' at ', ' ')
        html += f'''            <div class="video-item-large">
                <div class="video-container-large" onclick="zoomVideo(this)" style="cursor: pointer;">
                    <video id="video2_{slide_num}_{vid_idx}" controls>
                        <source src="{vid}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="video-caption">{caption}</div>
            </div>
'''
    
    html += '''        </div>
    </div>
</section>

'''
    slide_num += 1

# Save HTML
with open('complete_2nd_visit_slides.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated HTML for slides 4-{slide_num-1}")
print(f"Total new slides: {slide_num-4}")
print(f"File saved: complete_2nd_visit_slides.html")
