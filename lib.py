import cv2
import IPython
import numpy as np

def imshow(img):
    _,ret = cv2.imencode('.png', img)
    i = IPython.display.Image(data=ret)
    IPython.display.display(i)
