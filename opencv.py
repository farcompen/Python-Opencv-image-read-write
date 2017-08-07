#! /usr/bin python
# -*-coding:utf-8 -*-

import cv2
from matplotlib import pyplot as plt

def open_cv_ilk():
    res=cv2.imread("del.jpg", 0)
    cv2.imshow("resim", res)
    k=cv2.waitKey(0) &0xFF
    if k==27:
        cv2.destroyAllWindows()
    elif k==ord('s'):
        cv2.imwrite("del_gray.jpg", res)
        cv2.destroyAllWindows()
        print("yeni dosya kaydedildi")


def plot_uygulama():
    res=cv2.imread("del.jpg",0)
    plt.imshow(res, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()

open_cv_ilk()
plot_uygulama()
