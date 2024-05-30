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


def gerarHistogramaHsv(self):

    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Arquivos de imagem", ".png;.jpg;.jpeg;.bmp;.gif"), ("Todos os arquivos", ".*"))
    )

    janela = Toplevel(self)

    janela.geometry("400x300")

    SF.centerWindow(janela)

    button16Tons = tk.Button(janela, text="Gerar histograma com 16 tons de cinza", command= lambda: gerarCinza(file_path, 16))
    button16Tons.pack(pady=10)
    
    buttonFull = tk.Button(janela, text="Gerar histograma com 256 tons de cinza", command= lambda: gerarCinza(file_path, 256))
    buttonFull.pack(pady=10)

    buttonHSV = tk.Button(janela, text="Gerar histograma de cores no espaço HSV", command= lambda: gerarHsv(file_path, 0))
    buttonHSV.pack(pady=10)
    
    buttonHSV16 = tk.Button(janela, text="Gerar histograma de cores no espaço HSV (H=16 | V=8)", command= lambda: gerarHsv(file_path, 1))
    buttonHSV16.pack(pady=10)

    # hsv = gerarHsv(file_path)