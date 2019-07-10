import urllib.request
import cv2
import numpy as np
import os

def intros():
    
    f = open('links_neg.txt', 'r')
    neg_image_urls  = f.read()

    
    i = 1
    for linea in neg_image_urls.split('\n'):
        print(i)
        print(linea)
        i += 1
    f.close()

intros()