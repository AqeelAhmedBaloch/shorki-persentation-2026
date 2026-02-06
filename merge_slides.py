# Script to insert new slides into index.html
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with </section> for slide 3 (around line 283)
insert_position = None
for i, line in enumerate(lines):
    if 'data-slide="3"' in line:
        # Find the closing </section> for this slide
        for j in range(i, len(lines)):
            if '</section>' in lines[j]:
                insert_position = j + 1
                break
        break

print(f"Found insert position at line: {insert_position}")

# Read new slides
with open('new_slides.html', 'r', encoding='utf-8') as f:
    new_slides = f.readlines()

# Insert new slides
if insert_position:
    # Add newline before new slides
    new_content = lines[:insert_position] + ['\n'] + new_slides + ['\n'] + lines[insert_position:]
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_content)
    
    print("✅ Successfully inserted new slides!")
    print(f"Total lines: {len(lines)} -> {len(new_content)}")
else:
    print("❌ Could not find insert position")
