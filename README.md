#Скрипт для анализа рейтинга брендов по CSV-файлам.

##Запуск
### 1. Клонируйте проект:
```
git clone https://github.com/Lenger1117/test_workmate.git
```
### 2. Установите и активируйте виртуальное окружение:
```
python3 -m venv venv или python -m venv venv
```
```
source venv/bin/activate или source venv/Scripts/activate
```
### 3. Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### 4. Запуск скрипта:
```
python main.py --files examples/products1.csv examples/products2.csv --report average-rating
```
### 5. Запуск тестов:
```
pytest tests/ -v --cov=.
```
