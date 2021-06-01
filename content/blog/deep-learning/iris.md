---
title: 'TDC - Iris'
date: 2021-05-31 14:21:13
category: 'Deep-Learning'
draft: false
---

#Iris
    - tfds 사용

1. train, valid dataset load
    ```python
    train_dataset = tfds.load('iris', split='train[:80%]')
    valid_dataset = tfds.load('iris', split='train[80%:]')
    ```

2. 데이터 전처리 함수 생성 (one_hot)
    ```python
    def preprocess(data):
        x = data['features']
        y = data['label']
        y = tf.one_hot(y, 3)
        return x, y
    ```
   
3. 데이터 전처리와 batch size 설정
   ```python
   batch_size=10
   train_data = train_dataset.map(preprocess).batch(batch_size)
   valid_data = valid_dataset.map(preprocess).batch(batch_size)
   ```
   
4. 모델 생성
   ```python
   model = tf.keras.models.Sequential([
       Dense(512, activation='relu', input_shape=(4,)),
       Dense(256, activation='relu'),
       Dense(128, activation='relu'),
       Dense(64, activation='relu'),
       Dense(32, activation='relu'),
       Dense(3, activation='softmax'),
   ])
   ```
   
5. 모델 컴파일과 체크포인트 생성
   ```python
   model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
   checkpoint_path = "checkpoint.ckpt"
   checkpoint = ModelCheckpoint(filepath=checkpoint_path,
   save_weights_only=True,
   save_best_only=True,
   monitor='val_loss',
   verbose=1)
   ```
   
6. 학습
   ```python
   history = model.fit(train_data,
                    validation_data=(valid_data),
                    epochs=20,
                    callbacks=[checkpoint],
                   )
   model.save('iris.h5')
   model.load_weights(checkpoint_path)
   ```
   
7. 시각화
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
import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint

import matplotlib.pyplot as plt

train_dataset = tfds.load('iris', split='train[:80%]')
valid_dataset = tfds.load('iris', split='train[80%:]')

def preprocess(data):
    x = data['features']
    y = data['label']
    y = tf.one_hot(y, 3)
    return x, y
    
batch_size=10
train_data = train_dataset.map(preprocess).batch(batch_size)
valid_data = valid_dataset.map(preprocess).batch(batch_size)

model = tf.keras.models.Sequential([
    Dense(1024, activation='relu', input_shape=(4,)),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax'),
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
checkpoint_path = "checkpoint.ckpt"
checkpoint = ModelCheckpoint(filepath=checkpoint_path, 
                             save_weights_only=True, 
                             save_best_only=True, 
                             monitor='val_loss', 
                             verbose=1)
                             
history = model.fit(train_data,
                    validation_data=(valid_data),
                    epochs=20,
                    callbacks=[checkpoint],
                   )
                   
model.load_weights(checkpoint_path)  
model.save('iris.h5')

plt.figure(figsize=(12, 9))
plt.plot(np.arange(1, 21), history.history['loss'])
plt.plot(np.arange(1, 21), history.history['val_loss'])
plt.title('Loss / Val Loss', fontsize=20)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['loss', 'val_loss'], fontsize=15)
plt.show()

plt.figure(figsize=(12, 9))
plt.plot(np.arange(1, 21), history.history['loss'])
plt.plot(np.arange(1, 21), history.history['val_loss'])
plt.title('Loss / Val Loss', fontsize=20)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['loss', 'val_loss'], fontsize=15)
plt.show()
```