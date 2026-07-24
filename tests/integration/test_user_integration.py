def test_create_user(client):
    response = client.post(
        "/users",
        json={
            "username": "biggan_test",
            "email": "biggan_test_001@test.com"
        }
    )

    assert response.status_code == 200


def test_get_all_users(client):
    response = client.get("/users")

    assert response.status_code == 200


def test_get_user_by_id(client):
    response = client.get("/users/1")

    assert response.status_code == 200
