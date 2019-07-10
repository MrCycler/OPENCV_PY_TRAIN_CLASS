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
* Put links in links_neg.txt
* Execute:
    python download_neg_images_script.py

##Create bg.txt with images in neg
* Execute:
    python create_bg_txt.py

##Create samples with a positive img (watch5050.jpg)
* Create dir info

* Execute:
    opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
* Execute for create .vec:
    opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec

##Training of the classifier
* Create dir data

* Execute:
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20

* (Optional)
nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20 &

##Apply classifier 
* Copy .xml to root dir

* Execute:
    python apply_classifier_camera.py
or
    python apply_classifier_image.py

    need a imagen.jpg to detect