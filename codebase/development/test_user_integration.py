
import pytest
import json
from test_integration_config import test_app

def test_user_creation(test_app):
    with test_app.test_client() as client:
        response = client.post('/users/', data=json.dumps({'name': 'John Doe', 'email': 'john@example.com'}), content_type='application/json')
        assert response.status_code == 201
        assert 'application/json' in response.content_type
        data = json.loads(response.data.decode('utf-8'))
        assert data['name'] == 'John Doe'
        assert data['email'] == 'john@example.com'
