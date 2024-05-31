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
    plt.plot(histGrey, color='k')
    plt.title("Tons de Cinza")  
    plt.show() 

def gerarHsv(f, options):
    file_path = f
    # img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2HSV)

    f = plt.figure()

    names=['h', 's', 'v']
    # df = pd.read_table('data.txt', sep='\t',header=None, usecols=[0,1,2,3,4,5,6], names=['A', 'B', 'C', 'D','E','F','G'])

    fig, ax =plt.subplots()
    ax.plot(df['A'], df['B'], label='40 cm', linestyle='-', marker='o', color='DarkGreen', markersize=4)
    ax.plot(df['A'], df['C'], label='40 cm', linestyle='-', marker='o', color='MediumAquamarine', markersize=4)
    ax.plot(df['A'], df['D'], label='40 cm', linestyle='-', marker='o', color='OliveDrab', markersize=4)
    ax.plot(df['A'], df['E'], label='39 cm', linestyle='-', marker='o', color='OrangeRed', markersize=4)
    ax.plot(df['A'], df['F'], label='39 cm', linestyle='-', marker='o', color='Orange', markersize=4)
    ax.plot(df['A'], df['G'], label='39 cm', linestyle='-', marker='o', color='Coral', markersize=4)
    axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
    ax.set_xlabel('Tempo (minuto)', fontsize=15)
    ax.set_ylabel('Temperatura (ºC)', fontsize=15)
    ax.set_title('Perfil de temperatura do forno')
    ax.legend(loc=9, 
            bbox_to_anchor=(.75,.75),
            labelspacing=3,
            ncol=2, fontsize=14)

    trans = ax.get_xaxis_transform() # x em unidades do dado, y em fração do eixo
    ann = ax.annotate('Temperatura da zona quente', xy=(150, 0.75), xycoords=trans, fontsize=14)
    ann = ax.annotate('Temperatura da zona fria', xy=(150, 0.65), xycoords=trans, fontsize=14)
    ann = ax.annotate('Temperatura da zona termopar', xy=(150, 0.55), xycoords=trans, fontsize=14)

    if(options == 0):

        histr = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(histr, color='b')
        plt.xlim([0, 256])
        histr = cv2.calcHist([img], [1], None, [256], [0, 256])
        plt.plot(histr, color='g')
        plt.xlim([0, 256])
        histr = cv2.calcHist([img], [2], None, [256], [0, 256])
        plt.plot(histr, color='r')
        plt.xlim([0, 256])
            
        plt.title("Cores Normais")

    else:

        histr = cv2.calcHist([img], [0], None, [16], [0, 256])
        plt.plot(histr, color='b')
        plt.xlim([0, 16])
        histr = cv2.calcHist([img], [1], None, [8], [0, 256])
        plt.plot(histr, color='r')
        plt.xlim([0, 16])
            
        plt.title("Cores 16*8")

    # return plt
    plt.show()
