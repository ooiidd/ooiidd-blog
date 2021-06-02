# Question
#
# This task requires you to create a classifier for horses or humans using
# the provided data. Please make sure your final layer is a 1 neuron, activated by sigmoid as shown.
# Please note that the test will use images that are 300x300 with 3 bytes color depth so be sure to design your neural network accordingly

# =========== 합격 기준 가이드라인 공유 ============= #
# val_loss 기준에 맞춰 주시는 것이 훨씬 더 중요 #
# val_loss 보다 조금 높아도 상관없음. (언저리까지 OK) #
# =================================================== #
# 문제명: Category 3 - Horses Or Humans (Type B)
# val_loss: 0.51 (더 낮아도 안 좋고, 높아도 안 좋음!)
# val_acc: 관계없음
# =================================================== #
# =================================================== #



import tensorflow as tf
import urllib
import zipfile
import numpy as np
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import RMSprop

def solution_model():
    _TRAIN_URL = "https://storage.googleapis.com/download.tensorflow.org/data/horse-or-human.zip"
    _TEST_URL = "https://storage.googleapis.com/download.tensorflow.org/data/validation-horse-or-human.zip"
    urllib.request.urlretrieve(_TRAIN_URL, 'horse-or-human.zip')
    local_zip = 'horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_zip, 'r')
    zip_ref.extractall('tmp/horse-or-human/')
    zip_ref.close()
    urllib.request.urlretrieve(_TEST_URL, 'validation-horse-or-human.zip')
    local_zip = 'validation-horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_zip, 'r')
    zip_ref.extractall('tmp/validation-horse-or-human/')
    zip_ref.close()

    TRAINING_DIR = 'tmp/horse-or-human/'
    VALIDATION_DIR = 'tmp/validation-horse-or-human/'

    train_datagen = ImageDataGenerator(
      rescale=1/ 255.0,
      rotation_range=5,
      width_shift_range= 0.05,
      height_shift_range= 0.05,
      # shear_range= 0.2,
      zoom_range= 0.05,
      horizontal_flip= True,
      fill_mode='nearest',
    )
        #Your code here. Should at least have a rescale. Other parameters can help with overfitting.)

    validation_datagen = ImageDataGenerator(rescale=1/ 255.0,)

    train_generator = train_datagen.flow_from_directory(
        TRAINING_DIR,
        target_size=(300, 300),
        batch_size=128,
        class_mode='binary'
    )

    validation_generator = validation_datagen.flow_from_directory(
        VALIDATION_DIR,
        target_size=(300, 300),
        batch_size=32,
        class_mode='binary',
    )

    transfer_model = VGG16(weights='imagenet', include_top=False, input_shape=(300, 300, 3))
    transfer_model.trainable=False
    model = tf.keras.models.Sequential([
        transfer_model,
        Flatten(),
        Dropout(0.5),
        Dense(128, activation='relu'),
        Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])



    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

    checkpoint_path = "horse_checkpoint.ckpt"
    checkpoint = ModelCheckpoint(filepath=checkpoint_path,
                                save_weights_only=True,
                                save_best_only=True,
                                monitor='val_loss',
                                verbose=1)

    model.fit(train_generator,
              validation_data=(validation_generator),
              epochs=15,
              steps_per_epoch=8,
              callbacks=[checkpoint],
              )

    model.load_weights(checkpoint_path)

    # NOTE: If training is taking a very long time, you should consider setting the batch size appropriately on the generator, and the steps per epoch in the model.fit#
    return model


# Note that you'll need to save your model as a .h5 like this
# This .h5 will be uploaded to the testing infrastructure
# and a score will be returned to you
if __name__ == '__main__':
    model = solution_model()
    model.save("TF3-horses-or-humans-type-B.h5")