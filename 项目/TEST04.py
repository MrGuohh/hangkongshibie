import pandas as pd
import numpy as np
from keras.models import Sequential
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.saving.save import save_model

data = pd.read_csv('train_prepare.csv')
X = data.drop(['emd_lable2'], axis=1).values
y = data['emd_lable2'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(units=1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X_train, y_train, epochs=100, batch_size=32)


loss_and_metrics = model.evaluate(X_test, y_test, batch_size=128)

y_pred = model.predict(X_test)
print(y_pred)
# 保存整个模型
model.save('my_model.h5')
# 保存模型的权重
model.save_weights('my_model_weights.h5')