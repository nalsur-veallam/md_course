import pylab as plt
import matplotlib.image as mpimg

plt.figure(figsize=(15, 30))

fn = r'/home/user/md/first/first.png'
fn1 = r'/home/user/md/first/second.png'
fn2 = r'/home/user/md/first/third.png'
ims = []
ims.append(plt.imread(fn))
ims.append(plt.imread(fn1))
ims.append(plt.imread(fn2))

img1 = mpimg.imread('first.png')
img2 = mpimg.imread('second.png')
img3 = mpimg.imread('third.png')

plt.subplot (3, 1, 1)
plt.imshow(img1)
plt.title('Solid')
plt.subplot (3, 1, 2)
plt.imshow(img2)
plt.title('Phase transition')
plt.subplot (3, 1, 3)
plt.imshow(img3)
plt.title('Liquid')

plt.show()

#ax = plt.gca()
