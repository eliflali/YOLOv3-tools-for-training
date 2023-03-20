import os
#you have to put this python file in the same folder with the 'images' folder.
#this code is for use of 80% of images in training.
images  = os.listdir('images')
f = open("trained.txt", "w")
f2 = open("test.txt", "w")
a = 1
for image in images:
    pth = 'images/'+image
    neededpth = os.path.abspath(pth)
    if a%5 != 0:
        f.write(neededpth)
        f.write("\n")
    else:
        f2.write(neededpth)
        f2.write("\n")
    a+=1

f.close()
f2.close()


