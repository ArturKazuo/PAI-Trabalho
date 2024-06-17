# NF = 1
# NC = 1
# ND = 1.5

# Características usadas: Descritor de Haralick (3*6 características)

# O classificador: XGBoost

# O classificador profundo: EfficientNet

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from skimage.feature import hog
from skimage import io, color
import os
import shutil
import xgboost as xgb


from preProcess import delete_files_in_directory, preProcess

#divisão de imagens em conjuntos de treino e teste

# delete_files_in_directory('../classes/ASCH')
# delete_files_in_directory('../classes/ASCUS')
# delete_files_in_directory('../classes/LSIL')
# delete_files_in_directory('../classes/HSIL')
# delete_files_in_directory('../classes/Negative')
# delete_files_in_directory('../classes/SCC')

# preProcess()

def dividirImagens(className):

    # Definir diretórios
    source_dir = '../classes/' + className
    train_dir = '../classes/' + className + '/train'
    test_dir = '../classes/' + className + '/test'

    # Criar os diretórios de destino se não existirem
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Listar todas as imagens no diretório de origem
    all_images = os.listdir(source_dir)

    # Embaralhar a lista de imagens
    np.random.seed(42)  # Para reprodutibilidade
    np.random.shuffle(all_images)

    # Dividir as imagens em 80% para treinamento e 20% para teste
    split_index = int(len(all_images) * 0.8)
    train_images = all_images[:split_index]
    test_images = all_images[split_index:]

    # Mover imagens de treinamento
    for image in train_images:
        print(os.path.join(source_dir, image))
        print(image)
        print(os.path.join(train_dir, image))
        print(image)

        if(image != 'train' and image != 'test'):
            shutil.move(os.path.join(source_dir, image), os.path.join(train_dir, image))

    # Mover imagens de teste
    for image in test_images:
        if(image != 'train' and image != 'test'):
            shutil.move(os.path.join(source_dir, image), os.path.join(test_dir, image))

    print("Divisão concluída com sucesso!")






# dividirImagens("ASCH")
# dividirImagens("ASCUS")
# dividirImagens("HSIL")
# dividirImagens("LSIL")
# dividirImagens("Negative")
# dividirImagens("SCC")



# # Função fictícia para carregar dados - substitua isso com a função real
# def load_data():
#     # Supondo que temos 1000 amostras, 50 características por amostra e 6 classes
#     np.random.seed(42)
#     X = np.random.rand(1000, 50)
#     y = np.random.randint(0, 6, 1000)
#     return X, y

# # Carregar dados
# X, y = load_data()

# # Dividir dados em treino e teste
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # Classificador binário (classe 0 vs demais)
# y_train_bin = (y_train == 0).astype(int)
# y_test_bin = (y_test == 0).astype(int)

# clf_bin = SVC(kernel='linear', random_state=42)
# clf_bin.fit(X_train, y_train_bin)

# y_pred_bin = clf_bin.predict(X_test)
# acc_bin = accuracy_score(y_test_bin, y_pred_bin)
# cm_bin = confusion_matrix(y_test_bin, y_pred_bin)

# # Classificador multiclasse (6 classes)
# clf_multi = RandomForestClassifier(random_state=42)
# clf_multi.fit(X_train, y_train)

# y_pred_multi = clf_multi.predict(X_test)
# acc_multi = accuracy_score(y_test, y_pred_multi)
# cm_multi = confusion_matrix(y_test, y_pred_multi)

# # Função para plotar a matriz de confusão
# def plot_confusion_matrix(cm, title):
#     plt.figure(figsize=(8, 6))
#     sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
#     plt.xlabel('Predicted')
#     plt.ylabel('True')
#     plt.title(title)
#     plt.show()

# # Resultados
# print(f"Acurácia do classificador binário: {acc_bin:.2f}")
# plot_confusion_matrix(cm_bin, 'Matriz de Confusão - Classificador Binário')

# print(f"Acurácia do classificador multiclasse: {acc_multi:.2f}")
# plot_confusion_matrix(cm_multi, 'Matriz de Confusão - Classificador Multiclasse')


# Função para carregar dados e extrair HOG features
# def load_data(directory):
#     images = []
#     labels = []
#     for label in os.listdir(directory):
#         label_dir = os.path.join(directory, label)
#         if os.path.isdir(label_dir):
#             for file in os.listdir(label_dir):
#                 img_path = os.path.join(label_dir, file)
#                 image = io.imread(img_path)
#                 if len(image.shape) > 2:
#                     image = color.rgb2gray(image)
#                 images.append(image)
#                 labels.append(int(label))
#     return images, labels

# def extract_hog_features(images):
#     hog_features = []
#     for image in images:
#         fd = hog(image, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), multichannel=False)
#         hog_features.append(fd)
#     return np.array(hog_features)

# # Carregar dados
# source_dir = '../classes/ASCH'
# images, labels = load_data(source_dir)
# features = extract_hog_features(images)

# # Dividir dados em treino e teste
# X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# # Preparar os dados para o classificador binário (classe 0 vs demais)
# y_train_bin = (np.array(y_train) == 0).astype(int)
# y_test_bin = (np.array(y_test) == 0).astype(int)

# # Treinar o classificador XGBoost binário
# clf_bin = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
# clf_bin.fit(X_train, y_train_bin)

# # Predições e avaliação
# y_pred_bin = clf_bin.predict(X_test)
# acc_bin = accuracy_score(y_test_bin, y_pred_bin)
# cm_bin = confusion_matrix(y_test_bin, y_pred_bin)

# # Função para plotar a matriz de confusão
# def plot_confusion_matrix(cm, title):
#     plt.figure(figsize=(8, 6))
#     sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
#     plt.xlabel('Predicted')
#     plt.ylabel('True')
#     plt.title(title)
#     plt.show()

# # Resultados
# print(f"Acurácia do classificador binário: {acc_bin:.2f}")
# plot_confusion_matrix(cm_bin, 'Matriz de Confusão - Classificador Binário')