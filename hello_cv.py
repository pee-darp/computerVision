#! /usr/bin/python3
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from  PyQt5.QtGui import QImage, QPixmap
import cv2
import sys
import numpy as np

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(200,200,1920,1080)
    win.setWindowTitle("Hello ComputerVision!")

    label = QtWidgets.QLabel(win)
    label.setText("my first label is awesome")
    label.move(50,50)

    bgr_cv2_img = cv2.imread("rainbow.jpeg")
    rgb_cv2_img = cv2.cvtColor(bgr_cv2_img, cv2.COLOR_BGR2RGB)
    width,height = (200, 200)
    print(rgb_cv2_img)
    rgb_image = convertRGB2Qt(rgb_cv2_img, width, height)
    imageDisplay = createImageDisplay(win, width, height)
    imageDisplay.setPixmap(QPixmap.fromImage(rgb_image))
    win.show()
    sys.exit(app.exec_())

def convertRGB2Qt(img, width, height):
    try:
        frame = cv2.resize(img, (width, height))
        QtImg = QImage(frame,
                         frame.shape[1],
                         frame.shape[0],
                         QImage.Format_RGB888
                         )
        return QtImg
    except:
        return None

def createImageDisplay(window, width=640, height=480):
    try:
        imageDisplay = QtWidgets.QLabel(window)
        imageDisplay.setMinimumSize(QtCore.QSize(width, height))
        imageDisplay.setMaximumSize(QtCore.QSize(width, height))
        imageDisplay.setFrameShape(QtWidgets.QFrame.Box)
        return imageDisplay
    except:
        return None

window()
