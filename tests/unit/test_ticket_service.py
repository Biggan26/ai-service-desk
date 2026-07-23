from unittest.mock import MagicMock

from app.schemas.ticket import TicketCreate, TicketUpdate
from app.services.ticket_service import (
    create_ticket,
    delete_ticket,
    get_all_tickets,
    get_ticket_by_id,
    update_ticket,
)


def test_create_ticket():
    db = MagicMock()

    ticket = TicketCreate(
        title="Bug",
        description="Login issue",
        priority="High",
        assigned_to="Biggan",
        assigned_to_email="biggan@test.com",
    )

    result = create_ticket(db, ticket)

    assert result.title == "Bug"
    assert result.priority == "High"
    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()


def test_get_all_tickets():
    db = MagicMock()

    tickets = [MagicMock(id=1), MagicMock(id=2)]

    db.query.return_value.all.return_value = tickets

    result = get_all_tickets(db)

    assert result == tickets


def test_get_all_tickets_empty():
    db = MagicMock()

    db.query.return_value.all.return_value = []

    result = get_all_tickets(db)

    assert result == []


def test_get_ticket_by_id():
    db = MagicMock()

    ticket = MagicMock(id=1)

    db.query.return_value.filter.return_value.first.return_value = ticket

    result = get_ticket_by_id(db, 1)

    assert result == ticket


def test_get_ticket_by_id_not_found():
    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    result = get_ticket_by_id(db, 999)

    assert result is None


def test_get_ticket_by_negative_id():
    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    result = get_ticket_by_id(db, -1)

    assert result is None


def test_update_ticket():
    db = MagicMock()

    ticket = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = ticket

    data = TicketUpdate(
        title="Updated",
        description="Updated Desc",
        priority="Low",
        assigned_to="Alex",
        assigned_to_email="alex@test.com",
    )

    result = update_ticket(db, 1, data)

    assert result == ticket
    assert ticket.title == "Updated"
    db.commit.assert_called_once()
    db.refresh.assert_called_once()


def test_update_ticket_not_found():
    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    data = TicketUpdate(
        title="Updated",
        description="Updated Desc",
        priority="Low",
        assigned_to="Alex",
        assigned_to_email="alex@test.com",
    )

    result = update_ticket(db, 999, data)

    assert result is None


def test_delete_ticket():
    db = MagicMock()

    ticket = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = ticket

    result = delete_ticket(db, 1)

    assert result == ticket
    db.delete.assert_called_once_with(ticket)
    db.commit.assert_called_once()


def test_delete_ticket_not_found():
    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    result = delete_ticket(db, 999)

    assert result is None


def test_delete_ticket_negative_id():
    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    result = delete_ticket(db, -1)

    assert result is None
