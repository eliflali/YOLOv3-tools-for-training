import os

data = open("labeled.data", "w")
name = open("classes.names", "w")

##CLASSES##
#write number of classes existing#
data.write("classes=1\n")
data.write("train=")

##trainpath&testpath will be generated successfully if you used create_train.py##
trainpath = os.path.abspath("data/trained.txt")

data.write(trainpath)
data.write("\n")

testpath = os.path.abspath("data/test.txt")

data.write("valid=")
data.write(testpath)
data.write("\n")
#namespath will be generated successfullt, DO NOT NEED TO TOUCH##
namespath = os.path.abspath("data/classes.names")

data.write("names=")
data.write(namespath)
data.write("\n")

data.write("backup=backup")
##AFTER COMPLETING EVALUATION OF THIS CODE, GO TO classes.names
##AND CHANGE THE CONTENT ACCORDING TO YOUR DATA
##YOU HAVE TO WRITE CLASSES IN YOUR DATA
## ONE CLASS PER LINE ##
name.write("car")

