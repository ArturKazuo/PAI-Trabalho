import cv2
import numpy as np

def calculate_hu_moments(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calcula os momentos de Hu
    moments = cv2.moments(gray)
    hu_moments = cv2.HuMoments(moments).flatten()

    return hu_moments

