import urllib.request
import cv2
import sys
import numpy as np
import os

#Funcion para guardar imagenes de un listado
def store_raw_images(num_repeticiones):

    #procedente de un link
    #neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    #neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    
    #procedente de un listado
    f = open('links_neg.txt', 'r')
    neg_image_urls  = f.read()
    print("\n")
    pic_num = 1
    
    #crea carpeta neg
    if not os.path.exists('neg'):
        print("Creando carpeta neg")
        print("\n")
        os.makedirs('neg')

    #iteraciones   
    for j in range(0,int(num_repeticiones)):
        print('Iteracion del listado número: ',j+1)
        print("\n")  
    #iteracion para guardar imagenes del listado
        for i in neg_image_urls.split('\n'):
            try:
                print('Descargando: ',i)
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
        print("\n")
    print('Números de imagenes descargadas: ',pic_num-1)
    print("\n")
store_raw_images(sys.argv[1])