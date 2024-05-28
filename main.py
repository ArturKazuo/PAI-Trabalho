import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import csv
import cv2
import numpy as np
import os.path
import os
import matplotlib.pyplot as plt

from generateHistogramHSV import gerarHistograma
from preProcess import preProcess
from preProcess import delete_files_in_directory


def centerWindow(window, w, h):
  
  window_width = w
  window_height = h
  
  # get the screen dimension
  screen_width = window.winfo_screenwidth()
  screen_height = window.winfo_screenheight()

  # find the center point
  center_x = int(screen_width/2 - window_width / 2)
  center_y = int(screen_height/2 - window_height / 2)
  # set the position of the window to the center of the screen

  window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') # Uma f-string é uma string prefixada com a letra f ou F e permite incluir expressões Python dentro de chaves {} que são avaliadas em tempo de execução e formatadas usando a representação padrão dessas expressões.

def create_image_window(image, w, h):
    # Cria uma nova janela para exibir a imagem
    new_window = tk.Toplevel(janela)
    new_window.title("Imagem Selecionada")
    
    # Centraliza a nova janela
    centerWindow(new_window, w, h)
    
    # Cria um rótulo para exibir a imagem na nova janela
    image_label = tk.Label(new_window, image=image)
    image_label.image = image  # Mantém uma referência da imagem
    image_label.pack(pady=20)

def open_file():
    # Abre a caixa de diálogo para selecionar arquivos
    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Arquivos de imagem", ".png;.jpg;.jpeg;.bmp;.gif"), ("Todos os arquivos", ".*"))
    )
    
    if file_path:
        # Abre a imagem selecionada
        img = Image.open(file_path)

        # Obtém as dimensões originais da imagem
        width, height = img.size
        
        # Converte a imagem para um formato que o Tkinter pode exibir
        img_tk = ImageTk.PhotoImage(img)
        
        # Usa a função auxiliar para criar uma nova janela e exibir a imagem
        create_image_window(img_tk, width, height)
        
def open_file_black_white():
    # Abre a caixa de diálogo para selecionar arquivos
    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Arquivos de imagem", ".png;.jpg;.jpeg;.bmp;.gif"), ("Todos os arquivos", ".*"))
    )
    
    if file_path:
        # Abre a imagem selecionada
        img = Image.open(file_path)
        
        # Converte a imagem para tons de preto e cinza
        img = img.convert("L")

        # Obtém as dimensões originais da imagem
        width, height = img.size
        
        # Converte a imagem para um formato que o Tkinter pode exibir
        img_tk = ImageTk.PhotoImage(img)
        
        # Usa a função auxiliar para criar uma nova janela e exibir a imagem
        create_image_window(img_tk, width, height)
        

#comentar esse método para impedir o preprocessamento
# preProcess()

# Cria a janela principal
janela = tk.Tk()
centerWindow(janela, 400, 500)
janela.title("Home")

# Adiciona um rótulo à janela principal
label = tk.Label(janela, text="Home")
label.pack()

# Adiciona um botão à janela principal para selecionar uma imagem
buttonOpenImageWindow = tk.Button(janela, text="Selecionar imagem para visualizar", command=open_file)
buttonOpenImageWindow.pack(pady=10)

# Adiciona um botão à janela principal para selecionar uma imagem em preto e branco
buttonOpenImageWindowBlackWhite = tk.Button(janela, text="Selecionar imagem em tons de cinza para visualizar", command=open_file_black_white)
buttonOpenImageWindowBlackWhite.pack(pady=10)

buttonOpenHistogram = tk.Button(janela, text="Selecionar imagem para gerar o histograma", command=gerarHistograma)
buttonOpenHistogram.pack(pady=10)

# Inicia o loop principal do Tkinter
janela.mainloop()