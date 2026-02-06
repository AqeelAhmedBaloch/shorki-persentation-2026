# Insert new slides into index.html
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where to insert (after slide 3)
insert_position = None
for i, line in enumerate(lines):
    if '</section>' in line:
        # Check if this is after slide 3
        # Count how many </section> we've seen
        section_count = sum(1 for l in lines[:i+1] if '</section>' in l)
        if section_count == 3:  # After 3rd slide
            insert_position = i + 1
            break

print(f"Insert position: line {insert_position}")

# Read new slides
with open('complete_2nd_visit_slides.html', 'r', encoding='utf-8') as f:
    new_slides_html = f.read()

# Insert new slides
if insert_position:
    new_content = (
        ''.join(lines[:insert_position]) +
        '\n' + new_slides_html + '\n' +
        ''.join(lines[insert_position:])
    )
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully inserted 12 new slides!")
    print(f"Total slides now: 15")
else:
    print("ERROR: Could not find insert position")
