import requests


# Address of our Java Spring Boot API
BASE_URL = "http://localhost:8080/api/deliveries"


def test_get_all_deliveries():

    # Send a GET request to the Smart Logistics API
    response = requests.get(BASE_URL)

    # Check that the request was successful
    assert response.status_code == 200