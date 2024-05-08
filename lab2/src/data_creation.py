import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

# прочитаем датасет с ракушками из Github
df=pd.read_csv('https://raw.githubusercontent.com/Savirman/datasets/master/csv_result-abalone.csv', delimiter = ',')

# выделяем признаки и целевую переменную 'binaryClass'
X, y = df.drop(columns = ['binaryClass']), df['binaryClass']
# разбиваем на тренировочную и тестовю выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)

# сохраняем тренировочную и тестовую выборки в csv-файлы
train.to_csv('train/data_train.csv', index=False)
test.to_csv('test/data_test.csv', index=False)