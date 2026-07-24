from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from app.main import app
from app.database.database import get_db


mock_db = MagicMock()


def override_get_db():
    yield mock_db


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_user_api():
    mock_db.reset_mock()

    response = client.post(
        "/users",
        json={
            "username": "biggan",
            "email": "biggan@test.com"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "biggan"
    assert data["email"] == "biggan@test.com"

    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()


def test_get_all_users_api():
    mock_db.reset_mock()

    user1 = MagicMock(id=1, username="A", email="a@test.com")
    user2 = MagicMock(id=2, username="B", email="b@test.com")

    mock_db.query.return_value.all.return_value = [
        user1,
        user2,
    ]

    response = client.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2


def test_get_user_by_id_api():
    mock_db.reset_mock()

    user = MagicMock(
        id=1,
        username="biggan",
        email="biggan@test.com",
    )

    mock_db.query.return_value.filter.return_value.first.return_value = user

    response = client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "biggan"
    assert data["email"] == "biggan@test.com"


def test_get_user_not_found():
    mock_db.reset_mock()

    mock_db.query.return_value.filter.return_value.first.return_value = None

    response = client.get("/users/999")

    assert response.status_code == 200
    assert response.json() is None
