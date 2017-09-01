# change image type

import cv2
from PIL import Image
import os

folder = 'negative'
count=1237
# # adjust = 544
# while count < 54:
#     img = Image.open("Negative_vid/Clipboard%d.bmp" %count)
#     # new_img = img.resize( (256, 256) )
#     img.save('JPEG-NEG/neg%d.jpg' % adjust, 'jpeg')
#     count += 1
#     adjust += 1

for root, dirs, files in os.walk(folder):
    for i,f in enumerate(files):
        absname = os.path.join(root, f)
        newname = os.path.join(root, str('Khare_trainimage_negative_%d.jpg' % i))
        count=count-1
        os.rename(absname, newname)