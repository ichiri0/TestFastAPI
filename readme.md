# FastAPI Проект Менеджер Заметок

## Обзор

Это FastAPI-приложение, предоставляющее API-точки для управления пользователями и заметками. Проект организован с использованием API-роутеров (`api_v1`), включающих отдельные модули для сервисов, контроллеров и объектов передачи данных (DTO). Кроме того, существует модуль базы данных (`db`) с тестовыми данными.

## Структура проекта

- **api/v1/**
  - **users/**
    - `service.py` - Сервисные функции, связанные с пользователями
    - `controller.py` - Контроллеры API, связанные с пользователями
    - `dto.py` - Объекты передачи данных для сущностей пользователей
  - **notes/**
    - `service.py` - Сервисные функции, связанные с заметками
    - `controller.py` - Контроллеры API, связанные с заметками
    - `dto.py` - Объекты передачи данных для сущностей заметок
- **db/data/**
  - `test_data.py` - Тестовые данные для базы данных
- **main.py** - Основной исполняемый файл
- **settings.py** - Настройки проекта
- **requirements.txt** - Зависимости проекта
- **Dockerfile** - Файл конфигурации Docker
- **.dockerignore** - Файл игнорирования Docker
- **.gitignore** - Файл игнорирования Git

## API-точки

### API пользователей

- **GET /users/get-users/{user_id}**
  - Получение пользователя по ID.

- **GET /users/get-all-users/**
  - Получение всех пользователей.

### API заметок

- **GET /notes/get-note/{note_id}**
  - Получение заметки по ID.

- **GET /notes/get-note-by-user-id/{user_id}**
  - Получение всех заметок для конкретного пользователя.

## Запуск проекта

1. Установите зависимости с помощью `pip install -r requirements.txt`.
2. Запустите проект с помощью `python main.py`.

## Docker

Вы также можете запустить приложение в Docker-контейнере:

1. Соберите Docker-образ:

    ```bash
    docker build -t my-fastapi-app .
    ```

2. Запустите контейнер:

    ```bash
    docker run -p 4000:80 my-fastapi-app
    ```

Теперь ваше FastAPI-приложение будет работать в контейнере Docker, и его можно будет достучаться по порту 4000 на вашей локальной машине.