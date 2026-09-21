import requests

from config import BASE_URL


def test_filter_by_status():

    # Query parameters that will be added to the URL
    params = {
        "status": "PENDING"
    }

    # Send a GET request with the status filter
    response = requests.get(BASE_URL, params=params)

    # Check that the request was successful
    assert response.status_code == 200

    # Convert the JSON response into Python data
    deliveries = response.json()

    # At least one PENDING delivery should exist
    assert len(deliveries) > 0

    # Every returned delivery should have PENDING status
    for delivery in deliveries:
        assert delivery["status"] == "PENDING"


def test_filter_by_postcode():

    # Search using part of a postcode
    params = {
        "postcode": "M1"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200

    deliveries = response.json()

    assert len(deliveries) > 0

    # Every result should contain M1 in its postcode
    for delivery in deliveries:
        assert "M1" in delivery["postcode"]


def test_search_by_customer_name():

    # Use lowercase to check that the search is case-insensitive
    params = {
        "customerName": "john"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200

    deliveries = response.json()

    assert len(deliveries) > 0

    # Every returned customer name should contain "john"
    for delivery in deliveries:
        assert "john" in delivery["customerName"].lower()


def test_combined_filters():

    # Search using multiple filters at the same time
    params = {
        "status": "PENDING",
        "postcode": "M2",
        "customerName": "John"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200

    deliveries = response.json()

    assert len(deliveries) > 0

    # Check that every result matches all three filters
    for delivery in deliveries:
        assert delivery["status"] == "PENDING"
        assert "M2" in delivery["postcode"]
        assert "john" in delivery["customerName"].lower()