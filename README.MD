# Новостной портал
Новостной сайт на котором любой желающий может поделиться выдуманной новостью!

## Описание
Новостной сайт созданный с использованием микрофреймворка Flask в рамках обучения по программе Python Pro.

## Технологии
* Python
* Flask
* Flask-WTF
* Flask-SQLAlchemy

## Как запустить
1. Склонировать репозиторий
2. Создание и активация виртуального окружения
```commandline
python -m venv venv
GitBash: source venv/Scripts/activate
Windows: venv\Scripts\activate
Linux: source venv/bin/activate
```
3. Установка зависимостей
```commandline
pip install -r requirements.txt
```
4. Создайте файл .env и укажите настройки подключения к БД и другие параметры.
```text
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
5. Запуск Flask-приложения
```commandline
Без режима отладки: flask run
С режимом отладки: flask run --debug
```