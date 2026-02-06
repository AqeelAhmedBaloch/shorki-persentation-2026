with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find all slide sections
slide_starts = []
for i, line in enumerate(lines):
    if '<section class="slide"' in line and 'data-slide=' in line:
        # Extract slide number
        import re
        match = re.search(r'data-slide="(\d+)"', line)
        if match:
            slide_num = int(match.group(1))
            slide_starts.append((i, slide_num))

print(f"Found {len(slide_starts)} slides:")
for line_num, slide_num in slide_starts:
    print(f"  Line {line_num}: Slide {slide_num}")

# Find duplicate slides 4-7 (second occurrence)
seen_slides = set()
duplicates_to_remove = []

for line_num, slide_num in slide_starts:
    if slide_num in seen_slides and slide_num in [4, 5, 6, 7]:
        duplicates_to_remove.append((line_num, slide_num))
        print(f"\nDuplicate found: Slide {slide_num} at line {line_num}")
    seen_slides.add(slide_num)

if duplicates_to_remove:
    print(f"\nWill remove {len(duplicates_to_remove)} duplicate slides")
    
    # For each duplicate, find its start and end
    for start_line, slide_num in duplicates_to_remove:
        # Find the closing </section> for this slide
        end_line = None
        for i in range(start_line, len(lines)):
            if '</section>' in lines[i]:
                end_line = i
                break
        
        if end_line:
            print(f"  Slide {slide_num}: lines {start_line} to {end_line}")
    
    # Remove slides (from end to start to preserve line numbers)
    duplicates_to_remove.reverse()
    
    for start_line, slide_num in duplicates_to_remove:
        # Find end
        end_line = None
        for i in range(start_line, len(lines)):
            if '</section>' in lines[i]:
                end_line = i
                break
        
        if end_line:
            # Remove lines
            del lines[start_line:end_line+2]  # +2 to include </section> and blank line
            print(f"Removed duplicate Slide {slide_num}")
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"\nSuccessfully removed duplicate slides!")
    print(f"Total slides now: {len(slide_starts) - len(duplicates_to_remove)}")
else:
    print("\nNo duplicates to remove")
