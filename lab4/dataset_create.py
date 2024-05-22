import pandas as pd

# Создание словаря с данными
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

# Создание DataFrame из словаря
df = pd.DataFrame(data)

# Сохранение DataFrame в CSV файл
df.to_csv('datasets/dataset.csv', index=False)