from db.data.test_data import fake_users


async def get_user(user_id):
    for user in fake_users:
        if user["user_id"] == user_id:
            return user


async def get_all_users():
    return fake_users
