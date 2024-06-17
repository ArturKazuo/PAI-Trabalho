import tkinter as tk
import Screens.ScreenFacilities as SF
from PIL import Image , ImageTk
from hu import calculate_hu_moments
import cv2
import numpy as np
import tkinter.font as tkfont

class Screen_Hu(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        
        # ------------------------------
        #    Declaraçao de Variaveis
        # ------------------------------
        self.labels_hu = []
        for i in range(7):
            label = tk.Label(self)
            self.labels_hu.append(label)
        #------------------------------
        #   Configurações da janela
        #------------------------------

        self.title("Invariantes de Hu")
        self.geometry("500x300")
        SF.centerWindow(self)
        
        #------------------------------
        #        Componentes
        #------------------------------
        
        # Adiciona botões para calcular os momentos invariantes de Hu

        button_hu_RGB = tk.Button(self, text="Trocar imagem", command=lambda: escolher_imagem(tela = self),width=20, height=3,wraplength=100)
        button_hu_RGB.pack(pady=10,anchor="center")
        titulo = tk.Label(self,text="MOMENTOS INVARIANTES DE HU",font= tk.font.Font(family="Helvetica", size=14, weight="bold"))
        titulo.pack()
        for i in range(7):
            self.labels_hu[i].pack()
        

        

def exibir_hu_moments(image_path,tela = None):
    # Carregar a imagem
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Converter a imagem para o modelo HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_channel, s_channel, v_channel = cv2.split(hsv_image)

    # Calcular os momentos invariantes de Hu
    hu_moments_gray = calculate_hu_moments(gray_image)
    hu_moments_h = calculate_hu_moments(h_channel)
    hu_moments_s = calculate_hu_moments(s_channel)
    hu_moments_v = calculate_hu_moments(v_channel)
    
    for i in range(7):
        tela.labels_hu[i].configure(text="Momento"+ str(i+1) +  ": Cinza:"
                                    + str("{:.10f}".format(hu_moments_gray[i]))
                                    + " H: "
                                    + str("{:.10f}".format(hu_moments_h[i]))
                                    + " S: "
                                    + str("{:.10f}".format(hu_moments_s[i])) 
                                    + " V: "
                                    + str("{:.10f}".format(hu_moments_v[i])) )
def escolher_imagem(tela):
    file_path = tk.filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Arquivos de imagem", ".png;.jpg;.jpeg;.bmp;.gif"), ("Todos os arquivos", ".*"))
    )
    exibir_hu_moments(file_path,tela=tela)
       

