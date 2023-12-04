import sys
sys.path.append('..')
import json
import pytest
from ..hello import app  

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_tweet_success(client):
    tweet_data = {'text': 'This is a test tweet'}
    response = client.post('/tweets', json=tweet_data)
    assert response.status_code == 201  
    assert 'message' in response.json 

def test_create_tweet_failure(client):
    invalid_tweet_data = {'invalid_key': 'Missing text field'}
    response = client.post('/tweets', json=invalid_tweet_data)
    assert response.status_code == 400
    assert 'error' in response.json
