import tkinter as tk
import Screens.ScreenFacilities as SF
from PIL import Image , ImageTk

class Screen_ImageVisualizer(tk.Toplevel):
    def __init__(self, master=None,image=None):
        super().__init__(master)


        # ------------------------------
        #    Declaraçao de Variaveis
        # ------------------------------
        self.image_original = image
        tamanho_label_image = (400,400)
        self.image_colorida = image.resize(tamanho_label_image,Image.LANCZOS)
        self.image_cinza = (image.resize(tamanho_label_image,Image.LANCZOS)).convert("L")
        self.is_image_colorida = True
        self.label_imagem = tk.Label(self)
        self.painel_buttons = tk.Frame(self)
        self.button_change_color =  tk.Button(self.painel_buttons)

        # ------------------------------
        #    Configurações da pagina
        # ------------------------------
        self.title("Imagem Selecionada")



        # ------------------------------
        #    Configuração dos Widgets
        # ------------------------------
        # Label da imagem
        image_tk = ImageTk.PhotoImage(self.image_colorida)
        self.label_imagem.config(image=image_tk)
        self.label_imagem.image = image_tk

        # Botão para mudar a cor da imagem
        self.button_change_color.config(command=lambda: self.change_image_color())
        self.button_change_color.config(text = "Alterar cor da imagem")

        # ------------------------------
        #    Posicionamento dos Widgets
        # ------------------------------
        self.label_imagem.grid(column=0,row=0,pady=20)
        self.painel_buttons.grid(column=1,row=0)
        self.button_change_color.pack()

        



        # Centraliza a janela
        SF.centerWindow(self)
        
    def change_image_color(self):
        
        if not self.is_image_colorida:
            image_tk = ImageTk.PhotoImage(self.image_colorida)
            self.is_image_colorida = True
        elif self.is_image_colorida:
            image_tk = ImageTk.PhotoImage(self.image_cinza)
            self.is_image_colorida = False
        
        self.label_imagem.config(image= image_tk)
        self.label_imagem.image = image_tk
    
    