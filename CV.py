import matplotlib.pyplot as plt
import numpy as np
import cv2
import random
import os.path as pth

image = cv2.imread('original.png')

for i in range(1201):
    if pth.exists('C:\\Users\\admin\\Downloads\\test_dataset_test\\' + str(i) + '.png'):
        s1 = str(i)+".json"
        f = open(s1, "w")
        template = cv2.imread('C:\\Users\\admin\\Downloads\\test_dataset_test\\'+str(i)+ '.png')
        heat_map = cv2.matchTemplate(image, template, cv2.TM_SQDIFF_NORMED)

        h, w, _ = template.shape
        y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 5)

        left_top_x = x
        left_top_y = y
        right_top_x = left_top_x + w
        right_top_y = left_top_y
        left_bottom_x = left_top_x
        left_bottom_y = left_top_y + h
        right_bottom_x = x+w
        right_bottom_y = y+h
        angle = random.randint(0,360)
        s = "{\"left_top\": [" +str(left_top_x)+", "+str(left_top_y)+"], \"right_top\": ["+str(right_top_x)+", "+str(right_top_y)+"], \"left_bottom\": ["+str(left_bottom_x)+", "+str(left_bottom_y)+"], \"right_bottom\": ["+str(right_bottom_x)+", "+str(right_bottom_y)+"], \"angle\": "+str(angle)+"}"
        f.write(s)
        f.close()
        print(i)