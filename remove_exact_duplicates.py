import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all slide sections with their positions
slide_pattern = r'(<section class="slide" data-slide="\d+".*?</section>)'
matches = list(re.finditer(slide_pattern, content, re.DOTALL))

print(f"Found {len(matches)} slide sections\n")

# Identify duplicates to remove (second occurrence of slides 4-7)
seen_slides = set()
to_remove = []

for match in matches:
    slide_text = match.group(1)
    slide_num_match = re.search(r'data-slide="(\d+)"', slide_text)
    if slide_num_match:
        slide_num = int(slide_num_match.group(1))
        
        # If we've seen this slide before and it's 4-7, mark for removal
        if slide_num in seen_slides and slide_num in [4, 5, 6, 7]:
            to_remove.append(match)
            print(f"Marking for removal: Slide {slide_num} at position {match.start()}")
        
        seen_slides.add(slide_num)

print(f"\nTotal slides to remove: {len(to_remove)}")

# Remove duplicates (from end to start to preserve positions)
to_remove.reverse()
for match in to_remove:
    content = content[:match.start()] + content[match.end():]
    print(f"Removed slide at position {match.start()}")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
final_slides = re.findall(r'data-slide="(\d+)"', content)
print(f"\nFinal slide count: {len(final_slides)}")
print("Slide numbers:", sorted(set(int(s) for s in final_slides)))
