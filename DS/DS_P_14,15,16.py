# 01
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
sPicName='/content/drive/MyDrive/DS_PRACTICAL_NOTES/1.png'
t=0
img=mpimg.imread(sPicName)
print('Size:', img.shape)
plt.figure(figsize=(10, 10))
t+=1
sTitle= '(' + str(t) + ') Original'
plt.title(sTitle)
plt.imshow(img)
plt.show()
for c in range(img.shape[2]):
    t+=1
    plt.figure(figsize=(10, 10))
    sTitle= '(' + str(t) + ') Channel:' + str(c)
    plt.title(sTitle)
    lum_img = img[:,:,c]
    plt.imshow(lum_img)
    plt.show()


# 02
    import sys
import os
import matplotlib.pyplot as plt
from PIL import Image
sPicNameIn="/content/drive/MyDrive/DS_PRACTICAL_NOTES/1.png"
sPicNameOut="/content/audi.png"
imageIn = Image.open(sPicNameIn)
fig1 = plt.figure(figsize=(10, 10))
mask = imageIn.convert("L")
fig1.suptitle('Audi R8', fontsize=20)
imgplot = plt.imshow(imageIn)
th = 49
imageOut = mask.point(lambda i: i < th and 255)
imageOut.save(sPicNameOut)
imageTest = Image.open(sPicNameOut)
fig2=plt.figure(figsize=(10, 10))
fig2.suptitle('Audi R8 Edge', fontsize=20)
imgplot = plt.imshow(imageTest)


# 03
import sys
import os
import matplotlib.pyplot as plt
from PIL import Image
spicName = '/content/drive/MyDrive/DS_PRACTICAL_NOTES/1.png'
nSize = 4
img = Image.open(spicName)
plt.figure(figsize=(nSize, nSize))
sTitle = "Unchanges"
plt.title(sTitle)
imgplot = plt.imshow(img)



# 04
from PIL import Image
import matplotlib.pyplot as plt
# Load the image
img = Image.open("/content/drive/MyDrive/DS_PRACTICAL_NOTES/1.png")
# Thumbnail the image
img.thumbnail((64, 64), Image.ANTIALIAS)
# Resized image with Title
nSize = 10
sTitle = "Resized"
plt.figure(figsize=(nSize, nSize))
plt.title(sTitle)
imgplot = plt.imshow(img)
# Resized image with Bi-Cubic interpolation and Title
nSize = 10
sTitle = "Resized with Bi-Cubic"
plt.figure(figsize=(nSize, nSize))
plt.title(sTitle)
imgplot = plt.imshow(img, interpolation="bicubic")
print('### Done!! #########')