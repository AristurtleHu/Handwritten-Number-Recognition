# General purpose
import os
import numpy as np
from time import sleep
import time


# GPIO related
import RPi.GPIO as GPIO

# camera related
from picamera import PiCamera, Color

# GPIO mode: GPIO.BOARD, GPIO.BCM
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
# Close GPIO warning
GPIO.setwarnings(False)


# get the project path
PRJ_PATH = os.getcwd()

def image_split_column(img:np.ndarray)->list:
    """
    Function description: Splite the image by column. 
    Tips:
    1. Calculate the number of elements with a value of 255 in each column.
    2. When the number of 255 changes from zero to non-zero, it indicates the beginning of the digits area. Use startList to record the starting column index.
    3. When the number of 255 changes from non-zero to zero, it indicates the end of the digits area. Use endList to recorder the end column index.
    4. Use flag to represent the current state, outside or inside the digits area.
    
    :param img: input image to be splited by column.
    :return: output image after splited by column. It is a list, but its elements are np.ndarray.
    """
    
    # find out the number of columns in the original image
    # create a list to record the number of elements with a value of 255 in each column
    column = img.shape[1]
    columnHist = np.zeros(column)
    
    # initialize the variables
    flag = 0
    startList = []
    endList = []
    
    
    ### write your codes here ###
    #############################
    # step1:
    # count the number of elements with a value of 255 in each column and record it in columnHist
    # record the location where the the number of 255 changes in startList and endList
    # record the status with flag
    for i in range(column):
        count = np.count_nonzero(img[:, i:i+1] == 255)
        if count: flag = 1
        columnHist[i] = count
        if flag and len(endList) == len(startList): startList.append(i)
        elif flag == 0 and len(endList) < len(startList): endList.append(i)
        flag = 0
    if(len(endList) < len(startList)): endList.append(column + 1)
    # step 2:
    # following the startList and the endList, split the digits area from the original image.
    # there maybe several areas. recorder the areas in imgList and return imgList.
    imgList = []
    for i in range(len(startList)):
        imgList.append(img[:, startList[i]:endList[i]])
    return imgList



def image_split_row(img:np.ndarray)->list:
    """
    Function description: Splite the image by row. 
    Tips:
    1. Calculate the number of elements with a value of 255 in each row.
    2. When the number of 255 changes from zero to non-zero, it indicates the beginning of the digits area. Use startList to record the starting row index.
    3. When the number of 255 changes from non-zero to zero, it indicates the end of the digits area. Use endList to recorder the end row index.
    4. Use flag to represent the current state, outside or inside the digits area.
    
    :param img: input image to be splited by row.
    :return: output image after splited by row. It is a list, but its elements are np.ndarray.
    """
    
    # find out the number of rows in the original image
    # create a list to record the number of elements with a value of 255 in each row
    row = img.shape[0]
    rowHist = np.zeros(row)
    # initialize the variables
    flag = 0
    startList = []
    endList = [] 
    
    
    ### write your codes here ###
    #############################
    # step1:
    # count the number of elements with a value of 255 in each row and record it in rowHist
    # record the location where the the number of 255 changes in startList and endList
    # record the status with flag
    for i in range(row):
        count = np.count_nonzero(img[i] == 255)
        if count: flag = 1
        rowHist[i] = count
        if flag and len(endList) == len(startList): startList.append(i)
        elif flag == 0 and len(endList) < len(startList): endList.append(i)
        flag = 0
    if(len(endList) < len(startList)): endList.append(row + 1)
    # step 2:
    # following the startList and the endList, split the digits area from the original image.
    # there maybe several areas. recorder the areas in imgList and return imgList.    
    imgList = []     
    for i in range(len(startList)):
        imgList.append(img[startList[i]:endList[i]])
    return imgList


def led_display(numList:list)->None:
    """
    Function description: Build a digital tube display circuit on the breadboard. Display the result with the digital tube.
    Tips:
    1.The GPIO mode we used is GPIO.BOARD. 
    2.The digital tube is common anode. Use GPIO port to input high level for digital tube power pin.
    3. After the LED lamp pin of the digital tube is connected to the GPIO pin, the corresponding relationship can be confirmed by lighting the led one by one.
    4. Check "function introduction.xlsx" for GPIO functions.
    
    :para numList: input numbers in list to be displayed.
    :return: None
    """
    # change row wait for 2 seconds
    
    ### write your codes here ###
    #############################
    # step 1:
    # Clarify the relationship between led pins and GPIO pins
    # Set the GPIO pins to GPIO.OUT mode and give them the right output
    g = 8
    f = 10
    a = 12
    b = 16
    e = 22
    d = 24
    c = 26
    # step 2:
    # Clarify the led composition of each number
    num = [[a, f, b, e, c, d],[b, c],[a, b, g, e, d],[a, b, g, c, d],[f, g, b, c],[a, f, g, c, d],[a, f, g, e, c, d],[a, b, c],[a, f, b, g, e, c, d],[a, f, g, b, c, d]]  
    # step 3:
    # Display the numbers in the list one by one
    # Display every number for 1 second
    # Wait two seconds when displaying different lines
    for number in numList:
        for i in num[int(number)]:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)
        time.sleep(1)
        GPIO.cleanup()
        time.sleep(1)
    
    time.sleep(2)
    
    ret = None
    return ret


def take_photo()->str:
    """
    Function description: Build the camera control circuit on the breadboard. After pressing the control button, the shooting indicator(led light) lights up and the camera takes a picture.
    Tips:
    1. Use the 3.3v and GND pins on the Raspberry Pi as the power and ground of the circuit.
    2. Use the GPIO port as a signal line to sense the occurrence of key events. Set the correct GPIO mode
    3. Create a camera obj and wait for a button press to take a photo.
    4. Save the picture to /UserData/.
    5. Clean the camera.
    
    :para
    :return: a string which contains the picture location
    """

    ### write your codes here ###
    #############################
    # step 1: 
    #set a GPIO as an input channel for detecting
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(5, GPIO.OUT, initial = GPIO.HIGH)
    # step 2: 
    # create the camera obj and wait for a button to take a photo
    # recorder the saving path
    # clear the camera
    camera = PiCamera()
    camera.start_preview()
    state = GPIO.wait_for_edge(3, GPIO.FALLING, timeout = 100000)
    path = ""
    if state is None:
        print('Timeout occurred')
    else:
        GPIO.output(5, GPIO.LOW)
        time.sleep(2)
        path = "/home/pi/ProjectExercise/UserData/" + str(time.time()) + ".jpg"
        camera.capture(path)
    camera.stop_preview()
    camera.close()
    GPIO.cleanup()
    # step3:
    # return the saving path
    return path