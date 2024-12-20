# FastAPI_practice


## Описание:

Самое простое и бесполезно приложение на FastAPI, <br>
написанное для входной точки в понимании этого фреймворка. <br>

Так же в файле "deploy.txt" расписаны команды для развертывания приложения на сервере, <br>
используя Docker.

## Функционал:
- создание Тасков - список дел;
- получение Тасков.

## Инструменты:
- Python 3.x
- FastAPI
- aiosqlite
- Sqlalchemy

### Установка:
git clone https://github.com/gostok/FastAPI_practice.git <br>
cd FastAPI_practice <br>
pip install -r requirements.txt

### Запуск:
uvicorn main:app