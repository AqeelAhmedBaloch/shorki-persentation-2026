with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count all slides
import re
slides = re.findall(r'data-slide="(\d+)"', content)

print(f"Total slides found: {len(slides)}")
print("\nSlide numbers:")
for slide in slides:
    print(f"  Slide {slide}")

# Check if there are duplicate slides or old slides
if len(slides) != len(set(slides)):
    print("\n⚠️ WARNING: Duplicate slide numbers found!")
    
# Find slides 16-19 specifically
slides_16_19 = [s for s in slides if int(s) >= 16 and int(s) <= 19]
if slides_16_19:
    print(f"\n✓ Found slides to remove: {slides_16_19}")
else:
    print("\n✗ Slides 16-19 not found")
