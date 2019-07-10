import urllib.request
import cv2
import numpy as np
import os

#Funcion para guardar imagenes de un listado
def store_raw_images():

    #procedente de un link
    #neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    #neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    
    #procedente de un listado
    f = open('links_neg.txt', 'r')
    neg_image_urls  = f.read()

    pic_num = 1
    
    #crea carpeta
    if not os.path.exists('neg'):
        os.makedirs('neg')

    #iteracion para guardar imagenes del listado    
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            #se descarga la imagen
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            #se convierte a grises
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            #se escala tamaño
            resized_image = cv2.resize(img, (100, 100))
            #se guarda imagen
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  

store_raw_images()