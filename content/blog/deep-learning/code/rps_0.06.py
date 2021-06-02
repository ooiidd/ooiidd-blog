import urllib.request
import zipfile
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint

def solution_model():
  url = 'https://storage.googleapis.com/download.tensorflow.org/data/rps.zip'
  urllib.request.urlretrieve(url, 'rps.zip')
  local_zip = 'rps.zip'
  zip_ref = zipfile.ZipFile(local_zip, 'r')
  zip_ref.extractall('tmp/')
  zip_ref.close()


  TRAINING_DIR = "tmp/rps/"
  training_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=5,
    width_shift_range=0.05,
    height_shift_range=0.05,
    shear_range=0.05,
    zoom_range=0.03,
    horizontal_flip=True,
    fill_mode='reflect',
    validation_split=0.2
    )



  training_generator = training_datagen.flow_from_directory(TRAINING_DIR,
                                                            batch_size=128,
                                                            target_size=(150, 150),
                                                            class_mode='categorical',
                                                            subset='training',
                                                          )

  validation_generator = training_datagen.flow_from_directory(TRAINING_DIR,
                                                            batch_size=128,
                                                            target_size=(150, 150),
                                                            class_mode='categorical',
                                                            subset='validation',
                                                          )


  model = tf.keras.models.Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    # 2D -> 1D로 변환을 위하여 Flatten 합니다.
    Flatten(),
    # 과적합 방지를 위하여 Dropout을 적용합니다.
    Dropout(0.5),
    Dense(512, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
  ])

  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
  checkpoint_path = "tmp_checkpoint.ckpt"
  checkpoint = ModelCheckpoint(filepath=checkpoint_path,
                              save_weights_only=True,
                              save_best_only=True,
                              monitor='val_loss',
                              verbose=1)

  epochs=25

  history = model.fit(training_generator,
                      validation_data=(validation_generator),
                      epochs=epochs,
                      callbacks=[checkpoint],
                      )

  model.load_weights(checkpoint_path)




  return model
