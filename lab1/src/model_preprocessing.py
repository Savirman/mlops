import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler # Импортируем стандартизацию от scikit-learn
from sklearn.model_selection import train_test_split

# прочитаем из csv-файла подготовленный датасет для обучения
data_train = pd.read_csv('../train/data_train.csv')
X_train = data_train[['Length', 'Diameter', 'Height', 'Whole', 'Shucked', 'Viscera', 'Shell']]
y_train = data_train['binaryClass']

# Создаем объект StandardScaler
scaler = StandardScaler()

# Преобразуем данные в датафрейме с помощью StandardScaler
scaled_data = scaler.fit_transform(X_train)

# Преобразуем массив numpy обратно в датафрейм
scaled_df = pd.DataFrame(scaled_data, columns=X_train.columns)

X_train.to_csv('../train/X_train.csv', index=False)
y_train.to_csv('../train/y_train.csv', index=False)