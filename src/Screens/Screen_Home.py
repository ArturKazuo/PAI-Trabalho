import tkinter as tk
import Screens.ScreenFacilities as SF
from generateHistogramHSV import gerarHistogramaHsv

class HomeScreen(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #------------------------------
        #   Configurações da janela
        #------------------------------

        self.title("Home")
        self.geometry("400x300")
        self.configure(bg='lightblue')
        SF.centerWindow(self)

        #------------------------------
        #        Componentes
        #------------------------------

        # Adiciona um rótulo à janela principal
        label = tk.Label(self, text="Home")
        label.pack()

        # Adiciona um botão à janela principal para selecionar uma imagem
        buttonOpenImageWindow = tk.Button(self, text="Selecionar imagem para visualizar", command=lambda: SF.open_file())
        buttonOpenImageWindow.pack(pady=10)

        # Adiciona um botão à janela principal para selecionar uma imagem em preto e branco
        buttonOpenImageWindowBlackWhite = tk.Button(self, text="Selecionar imagem em tons de cinza para visualizar", command= lambda: SF.open_file_black_white())
        buttonOpenImageWindowBlackWhite.pack(pady=10)

        buttonOpenHistogram = tk.Button(self, text="Selecionar imagem para gerar o histograma",  command=lambda: gerarHistogramaHsv(self))
        buttonOpenHistogram.pack(pady=10)
        
       

