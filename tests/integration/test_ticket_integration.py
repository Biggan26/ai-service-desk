def test_create_ticket(client):
    response = client.post(
        "/tickets",
        json={
            "title": "Printer Issue",
            "description": "Printer is not working",
            "priority": "High",
            "assigned_to": "Biggan",
            "assigned_to_email": "biggan@test.com"
        }
    )

    assert response.status_code == 200


def test_get_all_tickets(client):
    response = client.get("/tickets")

    assert response.status_code == 200


def test_get_ticket_by_id(client):
    response = client.get("/tickets/1")

    assert response.status_code == 200
