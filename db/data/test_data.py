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

# Тестовые данные для заметок
fake_notes = [
    {"id": 1, "user_id": 1, "note": "Заметка 1 для пользователя 1", "is_completed": False},
    {"id": 2, "user_id": 1, "note": "Заметка 2 для пользователя 1", "is_completed": True},
    {"id": 3, "user_id": 1, "note": "Заметка 3 для пользователя 1", "is_completed": False},
    
    {"id": 4, "user_id": 2, "note": "Заметка 1 для пользователя 2", "is_completed": True},
    {"id": 5, "user_id": 2, "note": "Заметка 2 для пользователя 2", "is_completed": False},
    {"id": 6, "user_id": 2, "note": "Заметка 3 для пользователя 2", "is_completed": True},
    
    {"id": 7, "user_id": 3, "note": "Заметка 1 для пользователя 3", "is_completed": False},
    {"id": 8, "user_id": 3, "note": "Заметка 2 для пользователя 3", "is_completed": True},
    {"id": 9, "user_id": 3, "note": "Заметка 3 для пользователя 3", "is_completed": False},
    
    {"id": 10, "user_id": 4, "note": "Заметка 1 для пользователя 4", "is_completed": True},
    {"id": 11, "user_id": 4, "note": "Заметка 2 для пользователя 4", "is_completed": False},
    {"id": 12, "user_id": 4, "note": "Заметка 3 для пользователя 4", "is_completed": True},
    
    {"id": 13, "user_id": 5, "note": "Заметка 1 для пользователя 5", "is_completed": False},
    {"id": 14, "user_id": 5, "note": "Заметка 2 для пользователя 5", "is_completed": True},
    {"id": 15, "user_id": 5, "note": "Заметка 3 для пользователя 5", "is_completed": False},
    
    {"id": 16, "user_id": 6, "note": "Заметка 1 для пользователя 6", "is_completed": True},
    {"id": 17, "user_id": 6, "note": "Заметка 2 для пользователя 6", "is_completed": False},
    {"id": 18, "user_id": 6, "note": "Заметка 3 для пользователя 6", "is_completed": True},
    
    {"id": 19, "user_id": 7, "note": "Заметка 1 для пользователя 7", "is_completed": False},
    {"id": 20, "user_id": 7, "note": "Заметка 2 для пользователя 7", "is_completed": True},
    {"id": 21, "user_id": 7, "note": "Заметка 3 для пользователя 7", "is_completed": False},
    
    {"id": 22, "user_id": 8, "note": "Заметка 1 для пользователя 8", "is_completed": True},
    {"id": 23, "user_id": 8, "note": "Заметка 2 для пользователя 8", "is_completed": False},
    {"id": 24, "user_id": 8, "note": "Заметка 3 для пользователя 8", "is_completed": True},
    
    {"id": 25, "user_id": 9, "note": "Заметка 1 для пользователя 9", "is_completed": False},
    {"id": 26, "user_id": 9, "note": "Заметка 2 для пользователя 9", "is_completed": True},
    {"id": 27, "user_id": 9, "note": "Заметка 3 для пользователя 9", "is_completed": False},
    
    {"id": 28, "user_id": 10, "note": "Заметка 1 для пользователя 10", "is_completed": True},
    {"id": 29, "user_id": 10, "note": "Заметка 2 для пользователя 10", "is_completed": False},
    {"id": 30, "user_id": 10, "note": "Заметка 3 для пользователя 10", "is_completed": True},
    
    {"id": 31, "user_id": 11, "note": "Заметка 1 для пользователя 11", "is_completed": False},
    {"id": 32, "user_id": 11, "note": "Заметка 2 для пользователя 11", "is_completed": True},
    {"id": 33, "user_id": 11, "note": "Заметка 3 для пользователя 11", "is_completed": False},
    
    {"id": 34, "user_id": 12, "note": "Заметка 1 для пользователя 12", "is_completed": True},
    {"id": 35, "user_id": 12, "note": "Заметка 2 для пользователя 12", "is_completed": False},
    {"id": 36, "user_id": 12, "note": "Заметка 3 для пользователя 12", "is_completed": True},
    
    {"id": 37, "user_id": 13, "note": "Заметка 1 для пользователя 13", "is_completed": False},
    {"id": 38, "user_id": 13, "note": "Заметка 2 для пользователя 13", "is_completed": True},
    {"id": 39, "user_id": 13, "note": "Заметка 3 для пользователя 13", "is_completed": False},
    
    {"id": 40, "user_id": 14, "note": "Заметка 1 для пользователя 14", "is_completed": True},
    {"id": 41, "user_id": 14, "note": "Заметка 2 для пользователя 14", "is_completed": False},
    {"id": 42, "user_id": 14, "note": "Заметка 3 для пользователя 14", "is_completed": True},
    
    {"id": 43, "user_id": 15, "note": "Заметка 1 для пользователя 15", "is_completed": False},
    {"id": 44, "user_id": 15, "note": "Заметка 2 для пользователя 15", "is_completed": True},
    {"id": 45, "user_id": 15, "note": "Заметка 3 для пользователя 15", "is_completed": False},
    
    {"id": 46, "user_id": 16, "note": "Заметка 1 для пользователя 16", "is_completed": True},
    {"id": 47, "user_id": 16, "note": "Заметка 2 для пользователя 16", "is_completed": False},
    {"id": 48, "user_id": 16, "note": "Заметка 3 для пользователя 16", "is_completed": True},
    
    {"id": 49, "user_id": 17, "note": "Заметка 1 для пользователя 17", "is_completed": False},
    {"id": 50, "user_id": 17, "note": "Заметка 2 для пользователя 17", "is_completed": True},
    {"id": 51, "user_id": 17, "note": "Заметка 3 для пользователя 17", "is_completed": False},
    
    {"id": 52, "user_id": 18, "note": "Заметка 1 для пользователя 18", "is_completed": True},
    {"id": 53, "user_id": 18, "note": "Заметка 2 для пользователя 18", "is_completed": False},
    {"id": 54, "user_id": 18, "note": "Заметка 3 для пользователя 18", "is_completed": True},
    
    {"id": 55, "user_id": 19, "note": "Заметка 1 для пользователя 19", "is_completed": False},
    {"id": 56, "user_id": 19, "note": "Заметка 2 для пользователя 19", "is_completed": True},
    {"id": 57, "user_id": 19, "note": "Заметка 3 для пользователя 19", "is_completed": False},
    
    {"id": 58, "user_id": 20, "note": "Заметка 1 для пользователя 20", "is_completed": True},
    {"id": 59, "user_id": 20, "note": "Заметка 2 для пользователя 20", "is_completed": False},
    {"id": 60, "user_id": 20, "note": "Заметка 3 для пользователя 20", "is_completed": True},
]
