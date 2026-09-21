import requests

from config import BASE_URL

def test_get_all_deliveries():

    # Send a GET request to the Smart Logistics API
    response = requests.get(BASE_URL)

    # Check that the request was successful
    assert response.status_code == 200


def test_get_deliveries_returns_valid_data():

    # Send a GET request to retrieve all deliveries
    response = requests.get(BASE_URL)

    # Convert the JSON response into Python data
    deliveries = response.json()

    # Check that the API returned a list
    assert isinstance(deliveries, list)

    # Check that at least one delivery exists
    assert len(deliveries) > 0

    # Fields that every delivery should contain
    required_fields = {
        "id",
        "customerName",
        "address",
        "postcode",
        "status"
    }

    # Go through every delivery returned by the API
    for delivery in deliveries:

        # Check that all required fields are present
        assert required_fields.issubset(delivery.keys())


def test_get_delivery_by_id():

    # Send a GET request for delivery ID 1
    response = requests.get(f"{BASE_URL}/1")

    # Check that the delivery was found successfully
    assert response.status_code == 200

    # Convert the JSON response into a Python dictionary
    delivery = response.json()

    # Check the values returned by the API
    assert delivery["id"] == 1
    assert delivery["customerName"] == "John Smith"
    assert delivery["postcode"] == "M2 4AA"
    assert delivery["status"] == "PENDING"


def test_get_delivery_that_does_not_exist():

    # Request a delivery ID that does not exist
    response = requests.get(f"{BASE_URL}/999")

    # A missing delivery should return 404 Not Found
    assert response.status_code == 404

    # Convert the error response from JSON into Python data
    error_response = response.json()

    # Check the correct error message was returned
    assert error_response["error"] == "Delivery with ID 999 was not found"