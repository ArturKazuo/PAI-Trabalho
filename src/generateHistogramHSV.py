from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt

def gerarHsv(f):
    file_path = f
    img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2RGB)
    imgGrey = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2GRAY)
    histGrey = cv2.calcHist([imgGrey], [0], None, [256], [0, 256])
    plt.plot(histGrey, color='k')
    plt.title("Tons de Cinza")

    f = plt.figure()
    # # f.add_subplot(1, 2, 1)
    # # plt.imshow(img)
    # f.add_subplot(1, 2, 2)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
        
    plt.title("Cores")
    # return plt
    plt.show()


def gerarHistogramaHsv():

    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Arquivos de imagem", ".png;.jpg;.jpeg;.bmp;.gif"), ("Todos os arquivos", ".*"))
    )

    hsv = gerarHsv(file_path)