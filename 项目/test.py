import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

# 读取CSV文件
dataframe = pd.read_csv('new_data.csv')

# 将数据拆分为特征和标签
X = dataframe.drop('label', axis=1)
y = dataframe['label']

# 将标签转换为one-hot编码
y = tf.keras.utils.to_categorical(y)

# 将数据分为训练集和测试集
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2)

# 定义模型架构
model = tf.keras.Sequential([
  tf.keras.layers.Dense(32, activation='relu', input_shape=(784,)),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# 编译模型
model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# 训练模型
model.fit(train_X, train_y, epochs=10, validation_split=0.2)

# 在测试集上进行评估
test_loss, test_acc = model.evaluate(test_X, test_y, verbose=2)
print('Test accuracy:', test_acc)