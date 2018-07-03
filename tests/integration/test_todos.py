from tests.testutils.doubles import DatabaseDouble
from flasktest import app
import os
import tempfile

import pytest

@pytest.fixture
def client():
    # app.flasktestapp.config['TESTING'] = True
    app.flasktestapp.config['DATABASE'] = DatabaseDouble()
    client = app.flasktestapp.test_client()

    yield client


class TestToDoCrud:
    @property
    def database(client):
        return app.flasktestapp.config['DATABASE']

    def test_todo_list_empty(self, client):
        response = client.get('/')
        assert b'[]' in response.data

    def test_todo_list_with_preexistent_pending_todos(self, client):
        self.database.add_todo({
                               'name': 'Create a Flask example project',
                               'pending': True
                               })

        response = client.get('/')
        assert b'[{"name": "Create a Flask example project", "pending": true}]' in response.data

    def test_adds_todos(self, client):
        response = client.post('/',
                               json={
                                   'name': 'Look into HTOAS',
                                   'pending': True
                                   })

        assert '201 CREATED' == response.status
        assert len(self.database.all()) == 1, 'Should have added ToDo object to DB'

    def test_completes_todos(self, client):
        self.database.add_todo({'name': 'Should I be accessing the db?', 'pending': True})

        response = client.put('/1',
                              json={
                                  'name': 'Should I be accessing the db?',
                                  'pending': False
                              })

        assert '200 OK' == response.status
        assert len(self.database.all()) == 1, 'Should have same number of ToDos in DB'
        assert self.database.find(1) == {'name': 'Should I be accessing the db?', 'pending': False}, 'Should have completed ToDo'



