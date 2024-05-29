import tkinter as tk
import Screens.ScreenFacilities as SF

class Screen_ImageVisualizer(tk.Toplevel):
    def __init__(self, master=None,image=None):
        super().__init__(master)
        self.title("Imagem Selecionada")
    
    
        # Cria um rótulo para exibir a imagem na nova janela
        image_label = tk.Label(self, image=image)
        image_label.image = image  # Mantém uma referência da imagem
        image_label.pack(pady=20)
        # Centraliza a nova janela
        SF.centerWindow(self)
        