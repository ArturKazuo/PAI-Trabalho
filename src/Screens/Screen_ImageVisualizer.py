import tkinter as tk
import Screens.ScreenFacilities as SF
from PIL import Image , ImageTk
from Screens.Screen_Histograms import Screen_Histograms
from haralick import extract_glcm

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
        self.button_generate_haralick = tk.Button(self.painel_buttons)

        self.geometry("700x500")
        self.painel_imagem = tk.Frame(self)
        self.canvas_imagem = tk.Canvas(self.painel_imagem)
        self.label_imagem = tk.Label(self.canvas_imagem)

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

        #
        self.button_generate_haralick.config(text = "Calcular descritores de Haralick",command=lambda: self.generate_haralick(image_path = file_path_image))

        # ------------------------------
        #    Posicionamento dos Widgets
        # ------------------------------
       
        self.painel_buttons.grid(column=1,row=0)
        self.button_zoom_in.grid(column=0,row=0)
        self.button_zoom_out.grid(column=1,row=0)
        self.button_change_color.grid(column=0,row=1,pady=20,columnspan=2)
        self.button_generate_histogram.grid(column=0,row=2,pady=20,columnspan=2)
        self.button_generate_haralick.grid(column=0,row=3,pady=20,columnspan=2)

        



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

    def generate_haralick(self,image_path):
        # haralick_features(file_path_image = image_path)
        features = extract_glcm(image_path, distances=[5], angles=[0])

        self.show_haralick = tk.Toplevel() 
        # self.geometry("400x300")

        #insere todas as informações em uma caixa de texto para ser mostrada ao usuário
        text_box = tk.Text(self.show_haralick)
        text_box.pack()
        text_box.insert(tk.END, "Contraste: " + str(features[0][0]) + "\nHomogeneidade: " + str(features[0][1]) + "\nEntropia: " + str(features[1]))


        SF.centerWindow(self.show_haralick)

        # print(features)

    def config_image(self,zoom):

        # Resetando o MainFrame da imagem
        self.painel_imagem = tk.Frame(self,  width=500, height=400)
        self.painel_imagem.grid(column=0,row=0)

        # Resetando o Canvas da imagem
        self.canvas_imagem = tk.Canvas(self.painel_imagem,  width=500, height=400)
        self.canvas_imagem.grid(column=0,row=0)

        # Adicionando as duas scrollbars
        scrollbar_y = tk.Scrollbar(self.painel_imagem,
                                    orient="vertical",
                                    command=self.canvas_imagem.yview)
        scrollbar_y.grid(column=1,row=0,sticky="nsew")

        scrollbar_x = tk.Scrollbar(self.painel_imagem,
                                    orient="horizontal",
                                    command=self.canvas_imagem.xview)
        scrollbar_x.grid(column=0,row=1,sticky="nsew")

        # Configurando o Canvas
        self.canvas_imagem.configure(yscrollcommand=scrollbar_y.set,
                                     xscrollcommand=scrollbar_x.set)
        self.canvas_imagem.bind('<Configure>',lambda e: self.canvas_imagem.configure(scrollregion= self.canvas_imagem.bbox("all")))
        
        # Resetando o Label da imagem
        self.label_imagem = tk.Label(self.canvas_imagem)

        # Alocando o Label da imagem no canvas
        self.canvas_imagem.create_window((0,0),window=self.label_imagem,anchor="nw")

        # Conferindo a cor da imagem
        if self.is_image_colorida:
            image = self.image_colorida
        elif not self.is_image_colorida:
            image = self.image_cinza

        # Ajustando o zoom
        self.zoom+=zoom
        if(self.zoom)<=0:
            self.zoom = 1

        # Ajustando a imagem de acordo com o zoom
        image_tk = ImageTk.PhotoImage(image.resize((self.width_image* self.zoom, self.height_image * self.zoom)
                                                    ,Image.LANCZOS))
        self.label_imagem.config(image=image_tk)
        self.label_imagem.image = image_tk

    