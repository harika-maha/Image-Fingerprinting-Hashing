import os
from PIL import Image
import imagehash
import matplotlib.pyplot as plt


# Get all image paths in static folder
img_paths = [os.path.join('static', f) for f in os.listdir('static') if (f.endswith('.jpg') or (f.endswith('.jpeg')))]
# print(img_paths)

# Compare each pair of images
for i in range(len(img_paths)):
    for j in range(i+1, len(img_paths)):
        img1_path = img_paths[i]
        img2_path = img_paths[j]
        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)
        hash1 = imagehash.average_hash(img1)
        hash2 = imagehash.average_hash(img2)
        if hash1 - hash2<10:
            # Display similar images
            fig, axs = plt.subplots(1, 2)
            axs[0].imshow(img1)
            axs[0].set_title(f'Image {i+1}')
            axs[1].imshow(img2)
            axs[1].set_title(f'Image {j+1}')
            plt.show()