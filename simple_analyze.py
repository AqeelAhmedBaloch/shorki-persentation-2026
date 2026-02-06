import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find all slide sections
slides_found = []
for i, line in enumerate(lines):
    if 'data-slide=' in line:
        match = re.search(r'data-slide="(\d+)"', line)
        if match:
            slide_num = int(match.group(1))
            # Get title from next few lines
            title = "Unknown"
            for j in range(i, min(i+20, len(lines))):
                if 'slide-title' in lines[j] or 'main-title' in lines[j]:
                    title_match = re.search(r'>([^<]+)<', lines[j])
                    if title_match:
                        title = title_match.group(1).strip()
                        break
            
            slides_found.append({
                'line': i,
                'number': slide_num,
                'title': title
            })

print(f"Total slides: {len(slides_found)}\n")

# Group by slide number
from collections import defaultdict
by_number = defaultdict(list)
for slide in slides_found:
    by_number[slide['number']].append(slide)

# Print all slides
print("All slides:")
for slide in slides_found:
    print(f"  Line {slide['line']:4d}: Slide {slide['number']:2d} - {slide['title']}")

# Find duplicates
print("\n" + "="*80)
print("DUPLICATES:")
print("="*80)
duplicates = []
for num, occurrences in sorted(by_number.items()):
    if len(occurrences) > 1:
        print(f"\nSlide {num} appears {len(occurrences)} times:")
        for occ in occurrences:
            print(f"  Line {occ['line']}: {occ['title']}")
            duplicates.append(occ)

print(f"\n\nTotal duplicate sections: {len(duplicates)}")
print(f"Should have: 15 slides")
print(f"Currently have: {len(slides_found)} slides")
print(f"Need to remove: {len(slides_found) - 15} slides")
