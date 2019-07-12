## Create virtual enviroment
* Execute:
    virtualenv venvxtrainclass

## Activate
* Execute:
    source venvxtrainclass/bin/activate

##Install opencv
* Execute:
 pip3 install opencv-python

##Download images for neg
* Put links in links_neg.txt on root dir
* Execute (Specify number of iterations of lists):
    python download_neg_images_script.py 2

##Create bg.txt with images in neg, create dir info and dir pos
* Execute:
    python create_bg_txt.py

##Create samples with positives imgs
* Put positive images in pos dir

* For every positive example:
* Execute (-img pos/some_positive.jpg -num numero_de_ejemplos):
    opencv_createsamples -img pos/TRUCHA.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 68
* Execute (put the offset number)
    python change_info_files.py 0
* Copy images in other directory and eliminate info/info.lst

* Copy images and info.lst in dir info
* Execute for create .vec:
    opencv_createsamples -info info/info.lst -num 136 -w 20 -h 20 -vec positives.vec

##Training of the classifier
* Create dir data

* Execute:
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 136 -numNeg 68 -numStages 10 -w 20 -h 20

* (Optional)
nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 136 -numNeg 68 -numStages 10 -w 20 -h 20 &

##Apply classifier 
* Copy cascade.xml to root dir and rename it like object_cascade.xml

* Execute:
    python apply_classifier_camera.py
or
    python apply_classifier_image.py

    need a imagen.jpg in root dir to detect