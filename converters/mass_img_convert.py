from PIL import Image
import os


path = 'faces'
files = [os.path.join(path, x) for x in os.listdir(path)]
for f in files:
    img = Image.open(f)
    new_fname = f.replace('.bmp', '.jpg')
    img.save(new_fname, 'JPEG')
