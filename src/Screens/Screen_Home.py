import tkinter as tk
import Screens.ScreenFacilities as SF
from preProcess import preProcess

class HomeScreen(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        preProcess()
        
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


        
       

