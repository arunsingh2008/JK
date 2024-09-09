
import pytest
import json
from test_integration_config import test_app

def test_product_creation(test_app):
    with test_app.test_client() as client:
        response = client.post('/products/', data=json.dumps({'name': 'Widget', 'description': 'A useful widget', 'price': 9.99}), content_type='application/json')
        assert response.status_code == 201
        assert 'application/json' in response.content_type
        data = json.loads(response.data.decode('utf-8'))
        assert data['name'] == 'Widget'
        assert data['description'] == 'A useful widget'
        assert data['price'] == 9.99
