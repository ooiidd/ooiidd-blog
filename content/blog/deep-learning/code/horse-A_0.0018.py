# ======================================================================
# There are 5 questions in this test with increasing difficulty from 1-5
# Please note that the weight of the grade for the question is relative
# to its difficulty. So your Category 1 question will score much less
# than your Category 5 question.
# ======================================================================
#
# Computer Vision with CNNs
#
# This task requires you to create a classifier for horses or humans using
# the provided dataset.
#
# Please make sure your final layer has 2 neurons, activated by softmax
# as shown. Do not change the provided output layer, or tests may fail.
#
# IMPORTANT: Please note that the test uses images that are 300x300 with
# 3 bytes color depth so be sure to design your input layer to accept
# these, or the tests will fail.
#

# =========== 합격 기준 가이드라인 공유 ============= #
# val_loss 기준에 맞춰 주시는 것이 훨씬 더 중요 #
# val_loss 보다 조금 높아도 상관없음. (언저리까지 OK) #
# =================================================== #
# 문제명: Category 3 - Horses Or Humans type A
# val_loss: 0.028
# val_acc: 0.98
# =================================================== #
# =================================================== #


import tensorflow_datasets as tfds
import urllib.request
import zipfile
import numpy as np
from IPython.display import Image
from tensorflow.keras.applications import VGG16

import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import RMSprop

dataset_name = 'horses_or_humans'
# dataset, info = tfds.load(name=dataset_name, split=tfds.Split.TRAIN, with_info=True)
train_dataset = tfds.load(name=dataset_name, split='train[:80%]')
valid_dataset = tfds.load(name=dataset_name, split='train[80%:]')

print(train_dataset.take(1))
batch_size=10

def preprocess(data):
  x = data['image']
  y = data['label']
  return x, y

train_data = train_dataset.map(preprocess).batch(batch_size)
valid_data = valid_dataset.map(preprocess).batch(batch_size)


def solution_model():
  transfer_model = VGG16(weights='imagenet', include_top=False, input_shape=(300, 300, 3))
  transfer_model.trainable=False

  model = Sequential([
    Conv2D(16, (3, 3), activation='relu', input_shape=(300, 300, 3)),
    MaxPooling2D(2, 2),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    # 과적합 방지를 위하여 Dropout을 적용합니다.
    # Dropout(0.2),
    Dense(128, activation='relu'),
    Dense(32, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
  ])

  model.summary()

  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

  checkpoint_path = "cats-dog_checkpoint.ckpt"
  checkpoint = ModelCheckpoint(filepath=checkpoint_path,
              save_weights_only=True,
              save_best_only=True,
              monitor='val_loss',
              verbose=1)
  history = model.fit(train_data,
            validation_data=(valid_data),
            epochs=10,
            callbacks=[checkpoint],
            )

  model.load_weights(checkpoint_path)
  return model


# Note that you'll need to save your model as a .h5 like this
# This .h5 will be uploaded to the testing infrastructure
# and a score will be returned to you
if __name__ == '__main__':
    model = solution_model()
    model.save("TF3-horses-or-humans-type-A.h5")
