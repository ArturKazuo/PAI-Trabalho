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
        self.width_image = 400
        self.height_image = 400
        self.image_colorida = self.image_original.resize((self.width_image,self.height_image),Image.LANCZOS)
        self.image_cinza = (self.image_original.resize((self.width_image,self.height_image),Image.LANCZOS)).convert("L")
        self.is_image_colorida = True
        self.painel_buttons = tk.Frame(self)
        self.zoom = 1
        self.button_zoom_in = tk.Button(self.painel_buttons)
        self.button_zoom_out = tk.Button(self.painel_buttons)
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
        self.config_image(zoom=0)



        # Botão de zoom in
        self.button_zoom_in.config(text = "+",command=lambda: self.config_image(zoom=1))

        # Botão de zoom out
        self.button_zoom_out.config(text = "-",command=lambda: self.config_image(zoom=-1))


        # Botão para mudar a cor da imagem
        self.button_change_color.config(text = "Alterar cor da imagem",command=lambda: self.change_image_color())

        # Botão para gerar o histograma
        self.button_generate_histogram.config(text = "Gerar Histogramas",command=lambda: self.generate_histogram(image_path = file_path_image))

        # ------------------------------
        #    Posicionamento dos Widgets
        # ------------------------------
       
        self.painel_buttons.grid(column=1,row=0)
        self.button_zoom_in.grid(column=0,row=0)
        self.button_zoom_out.grid(column=1,row=0)
        self.button_change_color.grid(column=0,row=1,pady=20,columnspan=2)
        self.button_generate_histogram.grid(column=0,row=2,pady=20,columnspan=2)

        



        # Centraliza a janela
        SF.centerWindow(self)
        
    def change_image_color(self):
        
        if not self.is_image_colorida:
            image_tk = ImageTk.PhotoImage(self.image_colorida.resize((self.width_image* self.zoom, self.height_image * self.zoom)
                                                    ,Image.LANCZOS))
            self.is_image_colorida = True
        elif self.is_image_colorida:
            image_tk = ImageTk.PhotoImage(self.image_cinza.resize((self.width_image* self.zoom, self.height_image * self.zoom)
                                                    ,Image.LANCZOS))
            self.is_image_colorida = False
        
        self.label_imagem.config(image= image_tk)
        self.label_imagem.image = image_tk
    def generate_histogram(self,image_path):
        tela_histograma = Screen_Histograms(file_path_image = image_path)
    
    def config_image(self,zoom):
        # Criando um MainFrame
        self.painel_imagem = tk.Frame(self)
        self.painel_imagem.grid(column=0,row=0)

        # Criando um Canvas
        self.canvas_imagem = tk.Canvas(self.painel_imagem)
        self.canvas_imagem.grid(column=0,row=0)

        # Add a Scrollbar
        scrollbar_y = tk.Scrollbar(self.painel_imagem,
                                    orient="vertical",
                                    command=self.canvas_imagem.yview)
        scrollbar_y.grid(column=1,row=0,sticky="nsew")

        scrollbar_x = tk.Scrollbar(self.painel_imagem, orient="horizontal", command=self.canvas_imagem.xview)
        scrollbar_x.grid(column=0,row=1,sticky="nsew")

        # Configurando o Canvas
        self.canvas_imagem.configure(yscrollcommand=scrollbar_y.set,
                                     xscrollcommand=scrollbar_x.set)
        self.canvas_imagem.bind('<Configure>',lambda e: self.canvas_imagem.configure(scrollregion= self.canvas_imagem.bbox("all")))
        
        # Criando outro frame
        self.label_imagem = tk.Label(self.canvas_imagem)
  
        self.canvas_imagem.create_window((0,0),window=self.label_imagem,anchor="nw")
        if self.is_image_colorida:
            image = self.image_colorida
        elif not self.is_image_colorida:
            image = self.image_cinza

        self.zoom+=zoom
        if(self.zoom)<=0:
            self.zoom = 1

        
        image_tk = ImageTk.PhotoImage(image.resize((self.width_image* self.zoom, self.height_image * self.zoom)
                                                    ,Image.LANCZOS))
        
        self.label_imagem.config(image=image_tk)
        self.label_imagem.image = image_tk

    