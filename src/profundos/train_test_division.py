import os
import shutil
from sklearn.model_selection import train_test_split

# Defina os caminhos para as pastas de origem e destino
source_folder = 'PAI-Trabalho\classes'
train_folder = 'PAI-Trabalho\database\\treino'
test_folder = 'PAI-Trabalho\\database\\teste'

# Crie as pastas de destino, se não existirem
for subdir in ['ASCH', 'ASCUS', 'HSIL', 'LSIL', 'NEGATIVE', 'SCC']:
    os.makedirs(os.path.join(train_folder, subdir), exist_ok=True)
    os.makedirs(os.path.join(test_folder, subdir), exist_ok=True)

# Função para dividir e mover os arquivos
def split_and_move_files(class_name):
    class_path = os.path.join(source_folder, class_name)
    images = os.listdir(class_path)
    train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)
    
    for image in train_images:
        shutil.move(os.path.join(class_path, image), os.path.join(train_folder, class_name, image))
    
    for image in test_images:
        shutil.move(os.path.join(class_path, image), os.path.join(test_folder, class_name, image))

# Para cada classe, divida os arquivos e mova-os
for class_name in ['ASCH', 'ASCUS', 'HSIL', 'LSIL', 'NEGATIVE', 'SCC']:
    split_and_move_files(class_name)

print("Separação concluída.")