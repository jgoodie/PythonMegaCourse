# #!/usr/local/bin/python3
import numpy, cv2
n=numpy.arange(27)
print(n)
print(n.reshape(3,9))
print(n.reshape(3,3,3))

m=numpy.asarray([[100,100,100,100],[200,200,200,200],[300,300,300,300]])
print(m)
# grey scale
myimg=cv2.imread("smallgray.png",0)
print(myimg)
# color Blue, Green, Red
bgrimg = cv2.imread("smallgray.png",1)
print(bgrimg)

cv2.imwrite("newsmallgray.png",bgrimg)

# Indexing through a NumPy array
print(bgrimg[0,0,0])
print(bgrimg[0:3, 1, 1])
print(bgrimg[0])
for i in bgrimg:
    print(i)
    
for i in bgrimg.T: #transpose
    print(i)
for i in bgrimg.flat: #flatten
    print(i)
    
ims=numpy.hstack((myimg,myimg)) # takes a tuple
print(ims)
    
ims=numpy.vstack((myimg,myimg)) # takes a tuple
ims

lst=numpy.hsplit(ims,5)
print(lst)

