import os

# Count all images and videos in 2nd visit folder
base_path = r'c:\Users\Aqeel\Desktop\shorkipresentation\2nd visit'

images = []
videos = []

# Walk through directory
for root, dirs, files in os.walk(base_path):
    for file in files:
        ext = file.lower().split('.')[-1]
        rel_path = os.path.relpath(os.path.join(root, file), r'c:\Users\Aqeel\Desktop\shorkipresentation')
        
        if ext in ['jpg', 'jpeg', 'png']:
            images.append(rel_path)
        elif ext in ['mp4', 'mov', 'avi']:
            videos.append(rel_path)

print("="*80)
print("2ND VISIT MEDIA FILES")
print("="*80)

print(f"\nTotal Images: {len(images)}")
print(f"Total Videos: {len(videos)}")

print("\n" + "="*80)
print("IMAGES:")
print("="*80)
for i, img in enumerate(images, 1):
    print(f"{i:2d}. {img}")

print("\n" + "="*80)
print("VIDEOS:")
print("="*80)
for i, vid in enumerate(videos, 1):
    print(f"{i:2d}. {vid}")

# Calculate how many slides needed
# Each slide can show 6 images or 2 videos
images_per_slide = 6
videos_per_slide = 2

image_slides_needed = (len(images) + images_per_slide - 1) // images_per_slide
video_slides_needed = (len(videos) + videos_per_slide - 1) // videos_per_slide

print("\n" + "="*80)
print("SLIDES NEEDED:")
print("="*80)
print(f"Image slides: {image_slides_needed}")
print(f"Video slides: {video_slides_needed}")
print(f"Total media slides: {image_slides_needed + video_slides_needed}")

# Save paths to file
with open('media_files.txt', 'w', encoding='utf-8') as f:
    f.write("IMAGES:\n")
    for img in images:
        f.write(f"{img}\n")
    f.write("\nVIDEOS:\n")
    for vid in videos:
        f.write(f"{vid}\n")

print("\nPaths saved to media_files.txt")
