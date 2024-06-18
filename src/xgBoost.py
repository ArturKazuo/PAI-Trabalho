# NF = 1
# NC = 1
# ND = 1.5

# Características usadas: Descritor de Haralick (3*6 características)

# O classificador: XGBoost

# O classificador profundo: EfficientNet
from skimage import io, color
from skimage.feature import hog
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import xgboost as xgb
import numpy as np
import os
import shutil
import xgboost as xgb
from preProcess import delete_files_in_directory, preProcess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob

caminho_classes = "../classes/"
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
    source_dir = caminho_classes + className
    train_dir = caminho_classes + className + '/train'
    test_dir = caminho_classes + className + '/test'

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



def load_data(directory):
    images = []
    # print(directory)
    for label in os.listdir(directory):
        # print(label)
        label_dir = os.path.join(directory, label).replace("\\", "/")
        # print(os.path.isdir(label_dir))
        # if os.path.isdir(label_dir):
            # print("cheogu")
        # for file in os.listdir(label_dir):
        # img_path = os.path.join(label_dir, file)
        img_path = label_dir
        image = io.imread(img_path)
        print(image)
        if len(image.shape) > 2:
            image = color.rgb2gray(image)
        images.append(image)
        # labels.append(int(label))
    return images

# Function to extract HOG features
def extract_hog_features(images):
    hog_features = []
    for image in images:
        fd = hog(image, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), feature_vector=True)
        hog_features.append(fd)
    print(hog_features)
    return np.array(hog_features)

def train(className):

    # Load images and labels
    source_dir = '../classes/' + className + "/train"
    images = load_data(source_dir)

    # Extract HOG features
    features = extract_hog_features(images)

    print(images)
    print(features)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, test_size=0.2, random_state=42)

    # Train the XGBoost classifier
    clf = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    clf.fit(X_train, y_train)

    # Predict on the test set
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')

    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot confusion matrix
    def plot_confusion_matrix(cm, title):
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title(title)
        plt.show()

    plot_confusion_matrix(cm, 'Confusion Matrix')


train("ASCH")
train("ASCUS")
train("HSIL")
train("LSIL")
train("Negative")
train("SCC")


