import tkinter as tk
import Screens.ScreenFacilities as SF
from PIL import Image , ImageTk
from hu import calculate_hu_moments
import cv2
import numpy as np

class Screen_Hu(tk.Toplevel):
    def __init__(self, master=None,file_path_image=None):
        super().__init__(master)

        # ------------------------------
        #    Declaraçao de Variaveis
        # ------------------------------
        self.label_hu1 = tk.Label(self)
        self.label_hu2 = tk.Label(self)
        self.label_hu3 = tk.Label(self)
        self.label_hu4 = tk.Label(self)
        self.label_hu5 = tk.Label(self)
        self.label_hu6 = tk.Label(self)
        self.label_hu7 = tk.Label(self)
        #------------------------------
        #   Configurações da janela
        #------------------------------

        self.title("Invariantes de Hu")
        self.geometry("400x300")
        
        #------------------------------
        #        Componentes
        #------------------------------
        
        # Adiciona botões para calcular os momentos invariantes de Hu
        button_hu_gray = tk.Button(self, text="Momentos invariantes de Hu em tons de cinza", command=lambda: exibir_hu_moments_gray(file_path_image,tela = self) ,width=20, height=3,wraplength=100)
        button_hu_gray.pack(pady=10,anchor="center")
        button_hu_RGB = tk.Button(self, text="Momentos invariantes de Hu em canais de cor", command=lambda: exibir_hu_moments_RGB(file_path_image,tela = self),width=20, height=3,wraplength=100)
        button_hu_RGB.pack(pady=10,anchor="center")
        self.label_hu1.pack()
        self.label_hu2.pack()
        self.label_hu3.pack()
        self.label_hu4.pack() 
        self.label_hu5.pack()
        self.label_hu6.pack()
        self.label_hu7.pack()
        


def exibir_hu_moments_gray(image_path,tela = None):
    image = cv2.imread(image_path)
    hu_moments = calculate_hu_moments(image)

    tela.label_hu1.configure(text="Momento 1: " + str("{:.12f}".format(hu_moments[0])))
    tela.label_hu2.configure(text="Momento 2: " + str("{:.12f}".format(hu_moments[1])))
    tela.label_hu3.configure(text="Momento 3: " + str("{:.12f}".format(hu_moments[2])))
    tela.label_hu4.configure(text="Momento 4: " + str("{:.12f}".format(hu_moments[3])))
    tela.label_hu5.configure(text="Momento 5: " + str("{:.12f}".format(hu_moments[4])))
    tela.label_hu6.configure(text="Momento 6: " + str("{:.12f}".format(hu_moments[5])))
    tela.label_hu7.configure(text="Momento 7: " + str("{:.12f}".format(hu_moments[6])))

def exibir_hu_moments_RGB(image_path,tela = None):
    image = cv2.imread(image_path)
    b, g, r = cv2.split(image)
    hu_moments_b = calculate_hu_moments(cv2.merge([b, b, b]))
    hu_moments_g = calculate_hu_moments(cv2.merge([g, g, g]))
    hu_moments_r = calculate_hu_moments(cv2.merge([r, r, r]))
    
    tela.label_hu1.configure(text="Momento 1: R:"+str("{:.5f}".format(hu_moments_r[0])) + "  G:"+str("{:.5f}".format(hu_moments_g[0]))+"  B:"+str("{:.5f}".format(hu_moments_b[0])))
    tela.label_hu2.configure(text="Momento 2: R:"+str("{:.5f}".format(hu_moments_r[1])) + "  G:"+str("{:.5f}".format(hu_moments_g[1]))+"  B:"+str("{:.5f}".format(hu_moments_b[1])))
    tela.label_hu3.configure(text="Momento 3: R:"+str("{:.5f}".format(hu_moments_r[2])) + "  G:"+str("{:.5f}".format(hu_moments_g[2]))+"  B:"+str("{:.5f}".format(hu_moments_b[2])))
    tela.label_hu4.configure(text="Momento 4: R:"+str("{:.5f}".format(hu_moments_r[3])) + "  G:"+str("{:.5f}".format(hu_moments_g[3]))+"  B:"+str("{:.5f}".format(hu_moments_b[3])))
    tela.label_hu5.configure(text="Momento 5: R:"+str("{:.5f}".format(hu_moments_r[4])) + "  G:"+str("{:.5f}".format(hu_moments_g[4]))+"  B:"+str("{:.5f}".format(hu_moments_b[4])))
    tela.label_hu6.configure(text="Momento 6: R:"+str("{:.5f}".format(hu_moments_r[5])) + "  G:"+str("{:.5f}".format(hu_moments_g[5]))+"  B:"+str("{:.5f}".format(hu_moments_b[5])))
    tela.label_hu7.configure(text="Momento 7: R:"+str("{:.5f}".format(hu_moments_r[6])) + "  G:"+str("{:.5f}".format(hu_moments_g[6]))+"  B:"+str("{:.5f}".format(hu_moments_b[6])))

        
       

