import tkinter as tk
import Screens.ScreenFacilities as SF
from PIL import Image , ImageTk
import generateHistogramHSV as GH

class Screen_Histograms(tk.Toplevel):
    def __init__(self, master=None,file_path_image=None):
        super().__init__(master)
        self.geometry("400x300")

        button16Tons = tk.Button(self, text="Gerar histograma com 16 tons de cinza", command= lambda: GH.gerarCinza(file_path_image, 16))
        button16Tons.pack(pady=10)
        
        buttonFull = tk.Button(self, text="Gerar histograma com 256 tons de cinza", command= lambda: GH.gerarCinza(file_path_image, 256))
        buttonFull.pack(pady=10)

        buttonHSV = tk.Button(self, text="Gerar histograma de cores no espaço HSV", command= lambda: GH.gerarHsv(file_path_image, 0))
        buttonHSV.pack(pady=10)
        
        buttonHSV16 = tk.Button(self, text="Gerar histograma de cores no espaço HSV (H=16 | V=8)", command= lambda: GH.gerarHsv(file_path_image, 1))
        buttonHSV16.pack(pady=10)

        SF.centerWindow(self)