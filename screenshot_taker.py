import numpy as np
import pyautogui
import imutils
import cv2

image = pyautogui.screenshot(region=(0,0, 300, 400))

image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imshow('Screenshot', imutils.resize(image, width=600))

cv2.imwrite('pic.png', image)

image = cv2.imread('pic.png')
cv2.imshow('Screenshot', imutils.resize(image, width=600))
cv2.waitKey(0)