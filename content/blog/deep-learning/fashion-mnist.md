---
title: 'TDC - fashion mnist'
date: 2021-05-31 15:21:13
category: 'Deep-Learning'
draft: false
---

1. train, valid dataset load
    ```python
   fashion_mnist = tf.keras.datasets.fashion_mnist
   (x_train, y_train), (x_valid, y_valid) = fashion_mnist.load_data()
    ```

1. 정규화
    ```python
    x_train = x_train / 255.0
    x_valid = x_valid / 255.0
    ```
   
1. 모델 생성
   ```python
   model = Sequential([
       Flatten(input_shape=(28, 28)),
       Dense(1024, activation='relu'),
       Dense(512, activation='relu'),
       Dense(256, activation='relu'),
       Dense(128, activation='relu'),
       Dense(64, activation='relu'),
       Dense(10, activation='softmax'),
   ])
   ```
   
1. 모델 컴파일과 체크포인트 생성
   ```python
   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

   checkpoint_path = "checkpoint.ckpt"
   checkpoint = ModelCheckpoint(filepath=checkpoint_path,
   save_weights_only=True,
   save_best_only=True,
   monitor='val_loss',
   verbose=1)
   ```
   
1. 학습
   ```python
   history = model.fit(x_train, y_train,
                    validation_data=(x_valid, y_valid),
                    epochs=20,
                    callbacks=[checkpoint],
                   )
   
   model.save('mnist.h5')
   model.load_weights(checkpoint_path)
   #평가
   model.evaluate(x_valid, y_valid)
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
   ```text
   import numpy as np
   import matplotlib.pyplot as plt
   import tensorflow as tf
   
   from tensorflow.keras.layers import Dense, Flatten
   from tensorflow.keras.models import Sequential
   from tensorflow.keras.callbacks import ModelCheckpoint
   
   fashion_mnist = tf.keras.datasets.fashion_mnist
   (x_train, y_train), (x_valid, y_valid) = fashion_mnist.load_data()
   x_train.shape, x_valid.shape
   x_train.min(), x_train.max()
   
   #정규화
   x_train = x_train / 255.0
   x_valid = x_valid / 255.0
   
   # 시각화
   fig, axes = plt.subplots(2, 5)
   fig.set_size_inches(10, 5)
   
   for i in range(10):
       axes[i//5, i%5].imshow(x_train[i], cmap='gray')
       axes[i//5, i%5].set_title(str(y_train[i]), fontsize=15)
       plt.setp( axes[i//5, i%5].get_xticklabels(), visible=False)
       plt.setp( axes[i//5, i%5].get_yticklabels(), visible=False)
       axes[i//5, i%5].axis('off')
   
   plt.tight_layout()
   plt.show()
   
   x_train.shape
   
   #모델 생성
   model = Sequential([
       # Flatten으로 shape 펼치기(위의 x_train.shape)
       Flatten(input_shape=(28, 28)),
       # Dense Layer
       Dense(1024, activation='relu'),
       Dense(512, activation='relu'),
       Dense(256, activation='relu'),
       Dense(128, activation='relu'),
       Dense(64, activation='relu'),
       # Classification을 위한 Softmax 
       Dense(10, activation='softmax'),
   ])
   
   model.summary()
   
   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
   
   checkpoint_path = "checkpoint.ckpt"
   checkpoint = ModelCheckpoint(filepath=checkpoint_path, 
                                save_weights_only=True, 
                                save_best_only=True, 
                                monitor='val_loss', 
                                verbose=1)
                                
   history = model.fit(x_train, y_train,
                       validation_data=(x_valid, y_valid),
                       epochs=20,
                       callbacks=[checkpoint],
                      )
                      
                      
   model.save('mnist.h5')
   model.load_weights(checkpoint_path)
   model.evaluate(x_valid, y_valid)
   
   #오차 시각화
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