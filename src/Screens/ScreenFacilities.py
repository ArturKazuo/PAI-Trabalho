import tkinter as tk
from PIL import Image, ImageTk
from Screens.Screen_ImageVisualizer import Screen_ImageVisualizer


def open_file():
    # Abre a caixa de diálogo para selecionar arquivos
    file_path = tk.filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Arquivos de imagem", ".png;.jpg;.jpeg;.bmp;.gif"), ("Todos os arquivos", ".*"))
    )
    
    if file_path:
        # Abre a imagem selecionada
        img = Image.open(file_path)

        # Converte a imagem para um formato que o Tkinter pode exibir
        img_tk = ImageTk.PhotoImage(img)
        
        # Usa a função auxiliar para criar uma nova janela e exibir a imagem
        imagem_tela = Screen_ImageVisualizer(image = img_tk)

        
def open_file_black_white():
    # Abre a caixa de diálogo para selecionar arquivos
    file_path = tk.filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Arquivos de imagem", ".png;.jpg;.jpeg;.bmp;.gif"), ("Todos os arquivos", ".*"))
    )
    
    if file_path:
        # Abre a imagem selecionada
        img = Image.open(file_path)
        
        # Converte a imagem para tons de preto e cinza
        img = img.convert("L")
        
        # Converte a imagem para um formato que o Tkinter pode exibir
        img_tk = ImageTk.PhotoImage(img)
        
        # Usa a função auxiliar para criar uma nova janela e exibir a imagem
        imagem_tela = Screen_ImageVisualizer(image = img_tk)
       
        
def centerWindow(window):

    # Obter as dimensões da janela atual
    window.update_idletasks()  # Garantir que a janela tem as dimensões atualizadas
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    
    # Obter as dimensões da tela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular a posição central
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    
    # Definir a posição da janela no centro da tela sem alterar seu tamanho
    window.geometry(f'+{center_x}+{center_y}')


