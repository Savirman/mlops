import pandas as pd

# прочитаем из csv-файла подготовленный датасет для обучения
X_train = pd.read_csv('train/X_train.csv')
y_train = pd.read_csv('train/y_train.csv')
X_train = X_train[['Length', 'Diameter', 'Height', 'Whole', 'Shucked', 'Viscera', 'Shell']].values
y_train = y_train['binaryClass'].values
# загрузим модель машинного обучения
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=100_000).fit(X_train, y_train)

# сохраним обученную модель
import pickle
pickle.dump(model, open('model.pkl', 'wb'))