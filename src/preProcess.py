from PIL import Image, ImageTk
import cv2
import numpy as np
import os.path
import os
import matplotlib.pyplot as plt


def delete_files_in_directory(directory_path):
   try:
     with os.scandir(directory_path) as entries:
       for entry in entries:
         if entry.is_file():
            os.unlink(entry.path)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")

def createSubImages(line, img):   #usado para criar subimagens e armazená-las
    roi_x, roi_y, roi_width, roi_height = int(line[5]), int(line[6]), 100, 100  #pega os dados do nucleo
    roi = []

    h, w, c = img.shape
    
    if(roi_x >= 50 
       and roi_x <= w 
       and roi_y >= 50 
       and roi_y <= h
       ):
        roi = img[roi_y-50:roi_y+50, roi_x-50:roi_x+50]                             #cortar a imagem de um nucleo especifico

    elif(roi_x < 50 and roi_y < 50):
        roi = img[0:roi_y+50, 0:roi_x+50] 

    elif(roi_x < 50):
        roi = img[roi_y-50:roi_y+50, 0:roi_x+50] 

    elif(roi_x > w):
        return
    
    elif(roi_y < 50):
        roi = img[0:roi_y+50, roi_x-roi_x:roi_x+50] 

    elif(roi_y > h):
        return
    
    # print('\nstart\n')
    # print(roi)
    # print(roi_x)
    # print(roi_y)
    # if(len(roi) == 0):
    #     plt.subplot(1, 2, 1)
    #     plt.imshow(img)
    #     plt.title("Image with ROI")
    #     plt.show()
    # print('\nfinish\n')

    # cv2.rectangle(img, (roi_x-50, roi_y-50), (roi_x + 50, roi_y + 50), (0, 255, 0), 2)

    # image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)  #aplica cor para a subimagem

    # plt.subplot(1, 2, 1)
    # plt.imshow(image_rgb)
    # plt.title("Image with ROI")
    # plt.show()

    classImg = ''                                   #define a qual classe pertence o nucleo

    if(line[4] == 'ASC-US'):

        classImg = 'ASCUS'

    elif(line[4] == 'ASC-H'):

        classImg = 'ASCH'

    elif(line[4] == 'LSIL'):

        classImg = 'LSIL'

    elif(line[4] == 'HSIL'):

        classImg = 'HSIL'

    elif(line[4] == 'SCC'):

        classImg = 'SCC'

    elif(line[4] == 'Negative for intraepithelial lesion'):

        classImg = 'Negative'

    # print(type(line[0]))

    cv2.imwrite('../classes/' + classImg + "/" + line[3] + ".png", roi_rgb) #armazena a subimgem na sua classe correta

def preProcess():

    directory = "../classes"

    # cria os diretorios para armazenamento das classes
    if not os.path.exists(directory):
        # Create the directory
        os.makedirs(directory)
        print("Directory created successfully!")

        classes = [
            [], #Negative
            [], #ASCUS
            [], #ASCH
            [], #LSIL
            [], #HSIL
            []  #SCC
        ]

        directory1 = "../classes/Negative"
        directory2 = "../classes/ASCUS"
        directory3 = "../classes/ASCH"
        directory4 = "../classes/LSIL"
        directory5 = "../classes/HSIL"
        directory6 = "../classes/SCC"

        if not os.path.exists(directory1):
            os.makedirs(directory1)
        if not os.path.exists(directory2):
            os.makedirs(directory2)
        if not os.path.exists(directory3):
            os.makedirs(directory3)
        if not os.path.exists(directory4):
            os.makedirs(directory4)
        if not os.path.exists(directory5):
            os.makedirs(directory5)
        if not os.path.exists(directory6):
            os.makedirs(directory6)


    #deleta todas as imagens para testar o proprocessamento corretamente, vai ser retirado para a entrega
    delete_files_in_directory('../classes/ASCH')
    delete_files_in_directory('../classes/ASCUS')
    delete_files_in_directory('../classes/LSIL')
    delete_files_in_directory('../classes/HSIL')
    delete_files_in_directory('../classes/Negative')
    delete_files_in_directory('../classes/SCC')
    
    #abre e lê a planilha
    file = open('../database/classifications.csv')  
    content = file.readlines() 

    atual = ''              #atual é usado para checar se os nucleos são de uma mesma imagem ou não
    check_file = False      #check_file é usado para chacar se a imagem existe ou não no dataset
    img = []                #img é usado para armazenar o conteudo de uma imagem para que ela seja completamente preprocessada               

    # imgCount = 0            #imgCount é usado para contar quantas subimagens vão existir em uma determinada imagem

    for lines in content[1:len(content)]:           #itera sobre todas as linhas da planilha 

        line = lines.replace('\n', '').split(',')   #faz o parsing da linha para que os dados possam ser lidos facilmente

        if(line[1] != atual):                       #se o nome do arquivo for diferente do atual, significa que outra imagem deve ser lida

            # imgCount = 1                            #reseta o imgCount

            atual = line[1]                         #muda o atual

            # print(atual)

            check_file = os.path.isfile("../database/dataset/" + atual)   #checa para ver se o novo arquivo existe
            
            if(check_file):  
                print(atual)                                   #caso ele exista:
                img = cv2.imread("../database/dataset/" + atual)          #lê a nova imagem
                createSubImages(line, img)            #chama a primeira iteração do preprocessamento

        elif(check_file):                                       #chama mais preprocessamento até mudar de arquivo

            # imgCount += 1
            createSubImages(line, img)
        
    print("\n\n\nCHEGOU NO FINAL\n\n\n")

        
