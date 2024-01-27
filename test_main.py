from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_user():
    response = client.get("/users/get-users?user_id=1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1,
                               "first_name": "Джон", "last_name": "Безос"}


def test_read_all_users():
    response = client.get("/users/get-all-users")
    assert response.status_code == 200
    assert len(response.json()) == 20


def test_read_note():
    response = client.get("/notes/get-note?note_id=1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "user_id": 1, "note": "Заметка 1 для пользователя 1", "is_completed": False}


def test_read_note_by_user_id():
    response = client.get("/notes/get-note-by-user-id?user_id=1")
    assert response.status_code == 200
    assert len(response.json()) == 3
