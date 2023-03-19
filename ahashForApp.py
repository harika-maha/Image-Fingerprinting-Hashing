import os
from PIL import Image
import imagehash
import matplotlib.pyplot as plt

path = "/Users/sridhararunachalam/Desktop/FinalMiniProj/static/"
files_list = os.listdir("./static")
img_paths = [os.path.join('static', f) for f in os.listdir('static') if (f.endswith('.jpg') or (f.endswith('.jpeg')))]
def ahashing(img):

    hash1 = imagehash.average_hash(Image.open(path+img))
    print(hash1)
    
    hash_keys = dict()
    for index, filename in enumerate(files_list):
        img2 = Image.open(path+filename)
        hash2 = imagehash.average_hash(img2)
        hash_keys[hash2] = index
        
    # print(hash_keys)
    hash_values = []
    for key, value in hash_keys.items():
        hash_values.append(key)

    n = len(hash_keys)

    similar  =[]
    for i in range(n):
        img = i
        diff = hash1 - hash_values[i]
        if(diff < 10):
            similar.append(hash_keys.get(hash_values[img]))
    # print(similar)
    return similar