from flasktest import app
import os
import tempfile

import pytest
from tests.testutils.doubles import DatabaseDouble

@pytest.fixture
def client():
    # app.flasktestapp.config['TESTING'] = True
    print('****** client')
    app.flasktestapp.config['DATABASE'] = DatabaseDouble()
    client = app.flasktestapp.test_client()

    yield client


class TestToDoCrud:
    @property
    def database(client):
        return app.flasktestapp.config['DATABASE']

    def test_todos_journey(self, client):
        response = client.get('/')
        assert b'[]' in response.data
        client.post('/', json={'name': 'Look into HTOAS', 'pending': True})
        response = client.get('/')
        assert b'[{"name": "Look into HTOAS", "pending": true}]' in response.data, 'Should have added ToDo'

        client.put('/1',
                   json={
                      'name': 'Should I be accessing the db?',
                      'pending': False
                   })
        response = client.get('/')
        assert b'[{"name": "Look into HTOAS", "pending": false}]' in response.data, 'Should have updated ToDo'
