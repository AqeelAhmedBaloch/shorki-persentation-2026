import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all slide sections with their content
slide_pattern = r'<section class="slide" data-slide="(\d+)">(.*?)</section>'
slides = re.findall(slide_pattern, content, re.DOTALL)

print(f"Total slides found: {len(slides)}\n")

# Analyze each slide
slide_info = {}
for slide_num, slide_content in slides:
    # Get slide title
    title_match = re.search(r'<h[12] class="[^"]*title[^"]*">([^<]+)</h[12]>', slide_content)
    title = title_match.group(1) if title_match else "No title"
    
    # Check for duplicates
    if slide_num not in slide_info:
        slide_info[slide_num] = []
    
    slide_info[slide_num].append({
        'title': title,
        'content_length': len(slide_content)
    })

# Print analysis
print("="*80)
print("SLIDE ANALYSIS:")
print("="*80)

for slide_num in sorted(slide_info.keys(), key=int):
    occurrences = slide_info[slide_num]
    if len(occurrences) > 1:
        print(f"\n⚠️ DUPLICATE: Slide {slide_num} appears {len(occurrences)} times")
        for i, info in enumerate(occurrences, 1):
            print(f"  Occurrence {i}: '{info['title']}' ({info['content_length']} chars)")
    else:
        print(f"✓ Slide {slide_num}: '{occurrences[0]['title']}'")

# Count unique slides
unique_slides = len(slide_info)
total_slides = len(slides)

print("\n" + "="*80)
print(f"Unique slide numbers: {unique_slides}")
print(f"Total slide sections: {total_slides}")
print(f"Duplicates: {total_slides - unique_slides}")
print("="*80)
