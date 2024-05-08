#! /bin/bash

source venv/bin/activate

cd src

python3 data_creation.py

# Проверка на успешное выполнение data_creation.py
if [ $? -eq 0 ]; then
    # Если data_creation.py отработал успешно, запускаем model_preprocessing.py
    python3 model_preprocessing.py

    # Проверка на успешное выполнение model_preprocessing.py
    if [ $? -eq 0 ]; then
        # Если model_preprocessing.py отработал успешно, запускаем model_preparation.py
        python3 model_preparation.py

        # Проверка на успешное выполнение model_preparation.py
        if [ $? -eq 0 ]; then
            # Если model_preparation.py отработал успешно, запускаем model_testing.py
            python3 model_testing.py

            # Проверка на успешное выполнение model_testing.py
            if [ $? -ne 0 ]; then
                echo "Ошибка при выполнении model_testing.py"
            fi
        else
            echo "Ошибка при выполнении model_preparation.py"
        fi
    else
        echo "Ошибка при выполнении model_preprocessing.py"
    fi
else
    echo "Ошибка при выполнении data_creation.py"
fi