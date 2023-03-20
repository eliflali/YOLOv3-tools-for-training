# YOLOv3-tools-for-training
Codes I have written to make object detection with YOLOv3 easier. (Using any data set)

To use YOLOv3:

https://pjreddie.com/darknet/yolo/

In this website, there are all commands you need to write your Ubuntu terminal. However, for using on custom data set you aim to create, there are some changes you have to make.

Firstly:

At dataset folder, 

Delete trained.txt, test.txt, labeled.data and classes.names files. Those are added to create an example for you. 

1)create_train.py:  This script will make you able to create trained.txt and test.txt files which will make training your model possible later on. All you need to do is to put it in the same directory with your folder which is -strictly- named 'images'.

2)data_name.py: This script will create labeled.data and classes.names files. labeled.data will then be used for training and need to be carried under darknet/cfg folder.

Secondly:

You need to download darknet, yolov3.weights, and darknet53.conv.74 by using the link provided above. It is recommended to put yolov3.weights, and darknet53.conv.74 in folder 'weights' you are going to create. weights folder has to be in darknet folder.

Lastly:

Carry labeled.data file to darknet/cfg folder. 

Create your xxx.cfg file as told at darknet/cfg/configurations. The places I have made changes are commented in my yolov3_car_train.cfg file. Also, take a look at yolov3_car_test.cfg file. The only difference is between max_batches and subdivisions parameters between them. It is important to change classes parameter under [yolo] mark and filters parameter under [convolutions] mark. Even though they are marked, since the cfg file is too long, it may be forgotten. There are three of them. If you forget to change any of those, you will get an error which implies the parameter you forgot to change which is written in your .cfg file is not compatible with other parameters.

Be aware of the fact that those are not the only parameters, read darknet/cfg/configurations file carefully and proceed.

If you have succesfully completed all those steps, don't forget to install OpenCV to work with your model in real-time.

INSTALLING OpenCV and SOME PROBLEMS I HAVE GONE THROUGH:

Go to your darknet/Makefile file. Change OPENCV=1 at the beginning of the file. 

Download OpenCV with the repository:

https://github.com/jayrambhia/Install-OpenCV

Write the command 'make' again. Probably you will encounter some issues. Some links that helped me:

https://github.com/pjreddie/darknet/issues/1886#issuecomment-651644323

https://stackoverflow.com/questions/15320267/package-opencv-was-not-found-in-the-pkg-config-search-path

After the steps written in those links, try again. Worked for me.

TRAINING YOUR MODEL:

./darknet detector train cfg/labeled.data cfg/yolov3_car_train.cfg weights/darknet53.conv.74

This command will start training. NOTICE that your file's  name is probably different than yolov3_car_train.cfg, remember to change it.

After 100th and 200th epochs there will be weights files in your darknet/backup folder. They are to be used for detecting objects.

It is recommended to use an environment which can be created with Anaconda or any other similar distributions.








Thanks for reading till here. I hope this will make YOLOv3 experience better for you.





