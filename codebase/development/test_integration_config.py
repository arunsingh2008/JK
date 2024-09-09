
import pytest

@pytest.fixture(scope='session')
def test_app():
    from my_app import create_app
    app = create_app()
    app.config.update({
        'TESTING': True,
    })
    yield app
