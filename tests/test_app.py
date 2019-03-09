import os
import tempfile

import pytest

from app import app, DB_TYPE
from db import connection


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        connection.load_db_url(DB_TYPE)

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def empty_test(client):
    """Are we in the right universe?"""

    assert 1 == 1