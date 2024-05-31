import tkinter as tk
import Screens.ScreenFacilities as SF
from PIL import Image , ImageTk
from Screens.Screen_Histograms import Screen_Histograms

class Screen_ImageVisualizer(tk.Toplevel):
    def __init__(self, master=None,file_path_image=None):
        super().__init__(master)


        # ------------------------------
        #    Declaraçao de Variaveis
        # ------------------------------
        self.image_original = Image.open(file_path_image)
        tamanho_label_image = (400,400)
        self.image_colorida = self.image_original.resize(tamanho_label_image,Image.LANCZOS)
        self.image_cinza = (self.image_original.resize(tamanho_label_image,Image.LANCZOS)).convert("L")
        self.is_image_colorida = True
        self.label_imagem = tk.Label(self)
        self.painel_buttons = tk.Frame(self)
        self.button_change_color =  tk.Button(self.painel_buttons)
        self.button_generate_histogram = tk.Button(self.painel_buttons)

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
        self.button_change_color.config(text = "Alterar cor da imagem",command=lambda: self.change_image_color())

        # Botão para gerar o histograma
        self.button_generate_histogram.config(text = "Gerar Histogramas",command=lambda: self.generate_histogram(image_path = file_path_image))

        # ------------------------------
        #    Posicionamento dos Widgets
        # ------------------------------
        self.label_imagem.grid(column=0,row=0,pady=20)
        self.painel_buttons.grid(column=1,row=0)
        self.button_change_color.grid(column=0,row=0,pady=20)
        self.button_generate_histogram.grid(column=0,row=1,pady=20)

        



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
    def generate_histogram(self,image_path):
        tela_histograma = Screen_Histograms(file_path_image = image_path)
    