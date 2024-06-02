from PIL import Image
import cv2
import os
import glob
import csv
import numpy as np
from skimage import feature
from skimage import io, color, img_as_ubyte
from sklearn.metrics.cluster import entropy
from skimage.measure import shannon_entropy


def extract_glcm(image, distances, angles):
    print('[INFO] Extracting GLCM.')
    glcm_features = []

    file = cv2.imread(image)

    print(image)

    file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

    # extrai a matriz de co ocorrência 
    glcm = feature.graycomatrix(file, distances, angles, 256, symmetric=False, normed=True)

    #define quais propriedades devem ser extraidas da matriz de co ocorrencia
    glcm_properties = ['contrast', 'homogeneity']

    #extrai as informações
    features = [feature.graycoprops(glcm, glcm_property)[0, 0] for glcm_property in glcm_properties]

    #armazena as informações
    glcm_features.append(features)

    #calcula a entropia por ultimo
    entropy = shannon_entropy(file)

    glcm_features.append(entropy)

    print('\n')

    #retorna todos os descritores
    return glcm_features