import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.main import app
from app.database.database import get_db


@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def client(mock_db):
    def override_get_db():
        print(">>> USING MOCK DB <<<")
        yield mock_db

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
