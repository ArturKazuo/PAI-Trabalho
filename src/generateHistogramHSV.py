from tkinter import Toplevel, filedialog
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
import Screens.ScreenFacilities as SF

def gerarCinza(f, greyTones):
    file_path = f
    # img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2RGB)
    imgGrey = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2GRAY)
    histGrey = cv2.calcHist([imgGrey], [0], None, [greyTones], [0, 256])
    # print(histGrey)   
    plt.plot(histGrey, color='k')
    plt.title("Tons de Cinza")  
    plt.show() 

def gerarHsv(f, options):
    file_path = f
    # img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2HSV)

    f = plt.figure()

    if(options == 0):

        histr = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(histr, color='b')
        plt.xlim([0, 256])
        plt.plot(histr, label='Hue')
        histr = cv2.calcHist([img], [1], None, [256], [0, 256])
        plt.plot(histr, color='g')
        plt.xlim([0, 256])
        plt.plot(histr, label='Saturação')
        histr = cv2.calcHist([img], [2], None, [256], [0, 256])
        plt.plot(histr, color='r')
        plt.xlim([0, 256])
        plt.plot(histr, label='Valor')
            
        # Adicionando a legenda
        plt.legend()
        plt.title("Cores Normais")

    else:

        histr = cv2.calcHist([img], [0], None, [16], [0, 256])
        plt.plot(histr, color='b')
        plt.xlim([0, 16])
        plt.plot(histr, label='Hue')
        histr = cv2.calcHist([img], [1], None, [8], [0, 256])
        plt.plot(histr, color='r')
        plt.xlim([0, 16])
        plt.plot(histr, label='Valor')
            
        plt.legend()
        plt.title("Cores 16*8")

    # return plt
    plt.show()
