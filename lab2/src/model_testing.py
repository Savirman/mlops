import pickle
import pandas as pd
from sklearn.metrics import f1_score # f1-мера от Scikit-learn
from sklearn.metrics import classification_report # функция scikit-learn которая считает много метрик классификации

loaded_model = pickle.load(open('model.pkl', 'rb'))

# прочитаем из csv-файла подготовленный датасет для обучения
data_test = pd.read_csv('test/data_test.csv')
X_test = data_test[['Length', 'Diameter', 'Height', 'Whole', 'Shucked', 'Viscera', 'Shell']].values
y_test = data_test[['binaryClass']].values

# сделаем предсказание для первых 10 ракушек
print(loaded_model.predict(X_test[0:10]))