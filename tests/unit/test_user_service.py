from unittest.mock import MagicMock

from app.schemas.user import UserCreate
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
)


def test_create_user():
    db = MagicMock()

    user = UserCreate(
        username="biggan",
        email="biggan@test.com",
    )

    result = create_user(db, user)

    assert result.username == "biggan"
    assert result.email == "biggan@test.com"
    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()


def test_get_all_users():
    db = MagicMock()

    users = [MagicMock(id=1), MagicMock(id=2)]

    db.query.return_value.all.return_value = users

    result = get_all_users(db)

    assert result == users


def test_get_all_users_empty():
    db = MagicMock()

    db.query.return_value.all.return_value = []

    result = get_all_users(db)

    assert result == []


def test_get_user_by_id():
    db = MagicMock()

    user = MagicMock(id=1)

    db.query.return_value.filter.return_value.first.return_value = user

    result = get_user_by_id(db, 1)

    assert result == user


def test_get_user_by_id_not_found():
    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    result = get_user_by_id(db, 999)

    assert result is None


def test_get_user_by_negative_id():
    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    result = get_user_by_id(db, -1)

    assert result is None


def test_get_user_by_zero_id():
    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    result = get_user_by_id(db, 0)

    assert result is None
