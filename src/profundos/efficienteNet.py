import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Definindo diretórios
train_dir = 'PAI-Trabalho\database\\treino'
test_dir = 'PAI-Trabalho\database\\teste'

# Parâmetros
img_size = (224, 224)
batch_size = 32


train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Geradores de Imagem
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    classes=['NEGATIVE', 'ASCH', 'ASCUS', 'HSIL', 'LSIL', 'SCC']
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    classes=['NEGATIVE', 'ASCH', 'ASCUS', 'HSIL', 'LSIL', 'SCC']
)

#------------------------------
#---------Criar modelo---------
#------------------------------
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Carregar o modelo base
base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Congelar as camadas base
base_model.trainable = False

# Adicionar camadas superiores
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
x = Dense(1, activation='sigmoid')(x)

# Criar o modelo
model = Model(inputs=base_model.input, outputs=x)












model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Callbacks para salvar o melhor modelo e parar o treinamento cedo
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

checkpoint = ModelCheckpoint('best_model.keras', monitor='val_loss', save_best_only=True, mode='min')
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Treinar o modelo
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=test_generator,
    validation_steps=test_generator.samples // batch_size,
    epochs=5,
    callbacks=[checkpoint, early_stop]
)










import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Avaliação
test_loss, test_accuracy = model.evaluate(test_generator, steps=test_generator.samples // batch_size)
print(f'Test accuracy: {test_accuracy}')

# Predições
test_generator.reset()
predictions = model.predict(test_generator, steps=test_generator.samples // batch_size)
predicted_classes = np.where(predictions > 0.5, 1, 0)

# Verdadeiras classes
true_classes = test_generator.classes
class_labels = list(test_generator.class_indices.keys())

# Matriz de confusão
conf_matrix = confusion_matrix(true_classes, predicted_classes)

# Plotar matriz de confusão
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
#plt.xlabel('Predicted Label')
#plt.ylabel('True Label')
#plt.title('Confusion Matrix')
plt.show()

# Relatório de classificação
report = classification_report(true_classes, predicted_classes, target_names=class_labels)
print(report)











# Plotar a acurácia e perda de treino e validação
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(epochs, acc, 'r', label='Acurácia de treino')
plt.plot(epochs, val_acc, 'b', label='Acurácia de validação')
plt.title('Acurácia de treino e validação')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(epochs, loss, 'r', label='Perda de treino')
plt.plot(epochs, val_loss, 'b', label='Perda de validação')
plt.title('Perda de treino e validação')
plt.legend()

plt.show()

