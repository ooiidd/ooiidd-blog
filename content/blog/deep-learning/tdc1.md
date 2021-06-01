---
title: 'TDC(1)'
date: 2021-05-30 12:25:13
category: 'Deep-Learning'
draft: true
---

#기본 모델
학습은 전처리 -> 모델 생성 -> 학습 -> 검증 단계를 거친다.

### import
```
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
```

### 1. 데이터 전처리
```python
xs = np.array([-1.0 ,0.0 ,2.0 ,3.0, 4.0, 5.0, 6.0], dtype=float)
ys = np.array([1.0, 2.0 , 4.0, 5.0, 6.0, 7.0, 8.0], dtype=float)
```

### 2. 모델 생성
```python
model = Sequential([
    Dense(1, input_shape=[1]),
])

model.compile(optimizer='sgd', loss='mse')
```

### 3. 학습
```
model.fit(xs, ys, epochs=1200, verbose=0)
```

### 4. 검증
```
model.predict([102.0])
```
array([[104.001854]], dtype=float32)



##Dense Layer
Dense Layer는 Full Connected Layer이다.
