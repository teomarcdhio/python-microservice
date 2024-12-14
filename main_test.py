import json
# Import the main app from main.py
from main import app 
# Create a function to run the test
def test_index_route():
    response = app.test_client().get('/')
    res = json.loads(response.data.decode('utf-8'))
    # Assert response
    assert response.status_code == 200
    assert res['message'] == 'Hello, World!'
