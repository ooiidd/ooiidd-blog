---
title: 'TDC - cats & dogs'
date: 2021-06-1 13:21:13
category: 'Deep-Learning'
draft: false
---

- VGG16을 이용하여 전이학습으로 진행함.
- tensorflow-datasets를 활용.

***

1. dataset load
    ```python
   dataset_name = 'cats_vs_dogs'
   train_dataset = tfds.load(name=dataset_name, split='train[:80%]')
   valid_dataset = tfds.load(name=dataset_name, split='train[80%:]')
    ```

1. 전처리 함수 생성
   ```python
   def preprocess(data):
       x = data['image']
       y = data['label']
       # image 정규화(Normalization)
       x = x / 255
       # 사이즈를 (224, 224)로 변경
       x = tf.image.resize(x, size=(224, 224))
       return x, y
   ```
1. 데이터 전처리와 batch size 설정
   ```python
   batch_size=32
   train_data = train_dataset.map(preprocess).batch(batch_size)
   valid_data = valid_dataset.map(preprocess).batch(batch_size)
   ```
   
1. 모델 생성
   ```python
   transfer_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
   transfer_model.trainable=False
   
   model = Sequential([
       transfer_model,
       Flatten(),
       Dropout(0.5),
       Dense(512, activation='relu'),
       Dense(128, activation='relu'),
       Dense(2, activation='softmax'),
   ])
   
   model.summary()
   ```
   
1. 모델 컴파일과 체크포인트 생성
   ```python
   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
   
   checkpoint_path = "cats-dog_checkpoint.ckpt"
   checkpoint = ModelCheckpoint(filepath=checkpoint_path,
   save_weights_only=True,
   save_best_only=True,
   monitor='val_loss',
   verbose=1)
   ```
   
1. 학습
   - 학습 해 보니 epoch 7회차 넘어가면서 부터 overfitting이 심해서 10회로 돌려서 시간절약하는 것이 좋아보임.
   ```python
   history = model.fit(train_data,
          validation_data=(valid_data),
          epochs=10,
          callbacks=[checkpoint],
          )
   model.save('cats-dog.h5')
   model.load_weights(checkpoint_path)
   ```
   
1. 시각화
   ```python
   plt.figure(figsize=(12, 9))
   plt.plot(np.arange(1, 21), history.history['loss'])
   plt.plot(np.arange(1, 21), history.history['val_loss'])
   plt.title('Loss / Val Loss', fontsize=20)
   plt.xlabel('Epochs')
   plt.ylabel('Loss')
   plt.legend(['loss', 'val_loss'], fontsize=15)
   plt.show()
   
   plt.figure(figsize=(12, 9))
   plt.plot(np.arange(1, 21), history.history['acc'])
   plt.plot(np.arange(1, 21), history.history['val_acc'])
   plt.title('Acc / Val Acc', fontsize=20)
   plt.xlabel('Epochs')
   plt.ylabel('Acc')
   plt.legend(['acc', 'val_acc'], fontsize=15)
   plt.show()
   ```
   
8. 전체 소스
   ```python
   import numpy as np
   import tensorflow_datasets as tfds
   import matplotlib.pyplot as plt
   import tensorflow as tf
   
   from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
   from tensorflow.keras.models import Sequential
   from tensorflow.keras.callbacks import ModelCheckpoint
   from tensorflow.keras.applications import VGG16
   
   dataset_name = 'cats_vs_dogs'
   train_dataset = tfds.load(name=dataset_name, split='train[:80%]')
   valid_dataset = tfds.load(name=dataset_name, split='train[80%:]')
   
   def preprocess(data):
       x = data['image']
       y = data['label']
       # image 정규화(Normalization)
       x = x / 255
       # 사이즈를 (224, 224)로 변경
       x = tf.image.resize(x, size=(224, 224))
       return x, y
          
   batch_size=32
   train_data = train_dataset.map(preprocess).batch(batch_size)
   valid_data = valid_dataset.map(preprocess).batch(batch_size)
   transfer_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
   transfer_model.trainable=False
   
   model = Sequential([
       transfer_model,
       Flatten(),
       Dropout(0.5),
       Dense(512, activation='relu'),
       Dense(128, activation='relu'),
       Dense(2, activation='softmax'),
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
   model.save('cats-dog.h5')
   
   model.load_weights(checkpoint_path)
   
   plt.figure(figsize=(12, 9))
   plt.plot(np.arange(1, 21), history.history['loss'])
   plt.plot(np.arange(1, 21), history.history['val_loss'])
   plt.title('Loss / Val Loss', fontsize=20)
   plt.xlabel('Epochs')
   plt.ylabel('Loss')
   plt.legend(['loss', 'val_loss'], fontsize=15)
   plt.show()
   
   plt.figure(figsize=(12, 9))
   plt.plot(np.arange(1, 21), history.history['acc'])
   plt.plot(np.arange(1, 21), history.history['val_acc'])
   plt.title('Acc / Val Acc', fontsize=20)
   plt.xlabel('Epochs')
   plt.ylabel('Acc')
   plt.legend(['acc', 'val_acc'], fontsize=15)
   plt.show()
   ```