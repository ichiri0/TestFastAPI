
# Тестовый лист с данными пользователя
fake_users = [
    {"user_id": 1, "first_name": "Джон", "last_name": "Безос"},
    {"user_id": 2, "first_name": "Бэн", "last_name": "Аффлек"},
    {"user_id": 3, "first_name": "Мишель", "last_name": "Робертс"},
    {"user_id": 4, "first_name": "Эмма", "last_name": "Стоун"},
    {"user_id": 5, "first_name": "Лиам", "last_name": "Нисон"},
    {"user_id": 6, "first_name": "Натали", "last_name": "Портман"},
    {"user_id": 7, "first_name": "Джейк", "last_name": "Джилленхол"},
    {"user_id": 8, "first_name": "Анджелина", "last_name": "Джоли"},
    {"user_id": 9, "first_name": "Райан", "last_name": "Гослинг"},
    {"user_id": 10, "first_name": "Шарлиз", "last_name": "Терон"},
    {"user_id": 11, "first_name": "Том", "last_name": "Харди"},
    {"user_id": 12, "first_name": "Марго", "last_name": "Робби"},
    {"user_id": 13, "first_name": "Крис", "last_name": "Хемсворт"},
    {"user_id": 14, "first_name": "Аманда", "last_name": "Сайфред"},
    {"user_id": 15, "first_name": "Роберт", "last_name": "Дауни мл."},
    {"user_id": 16, "first_name": "Эмили", "last_name": "Блант"},
    {"user_id": 17, "first_name": "Кристиан", "last_name": "Бейл"},
    {"user_id": 18, "first_name": "Марк", "last_name": "Уолберг"},
    {"user_id": 19, "first_name": "Дайан", "last_name": "Крюгер"},
    {"user_id": 20, "first_name": "Киану", "last_name": "Ривз"},
]


async def get_user(user_id):
    for user in fake_users:
        if user["user_id"] == user_id:
            return user


async def get_all_users():
    return fake_users
