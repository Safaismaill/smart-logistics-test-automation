import requests

from config import BASE_URL


def test_create_delivery():

    # Data that will be sent to the Java API
    new_delivery = {
        "customerName": "Test Customer",
        "address": "50 Test Street",
        "postcode": "M3 1AA",
        "status": "PENDING"
    }

    # Send the delivery data as JSON
    response = requests.post(
        BASE_URL,
        json=new_delivery
    )

    # Check that the delivery was created successfully
    assert response.status_code == 200

    created_delivery = response.json()

    # Check that an ID was generated
    assert created_delivery["id"] is not None

    # Check returned values
    assert created_delivery["customerName"] == "Test Customer"
    assert created_delivery["address"] == "50 Test Street"
    assert created_delivery["postcode"] == "M3 1AA"
    assert created_delivery["status"] == "PENDING"

    # Clean up the test delivery
    delivery_id = created_delivery["id"]

    delete_response = requests.delete(
        f"{BASE_URL}/{delivery_id}"
    )

    assert delete_response.status_code == 200


def test_create_delivery_with_blank_customer_name():

    invalid_delivery = {
        "customerName": "",
        "address": "50 Test Street",
        "postcode": "M3 1AA",
        "status": "PENDING"
    }

    response = requests.post(
        BASE_URL,
        json=invalid_delivery
    )

    assert response.status_code == 400


def test_create_delivery_with_blank_address():

    invalid_delivery = {
        "customerName": "Test Customer",
        "address": "",
        "postcode": "M3 1AA",
        "status": "PENDING"
    }

    response = requests.post(
        BASE_URL,
        json=invalid_delivery
    )

    assert response.status_code == 400


def test_create_delivery_with_blank_postcode():

    invalid_delivery = {
        "customerName": "Test Customer",
        "address": "50 Test Street",
        "postcode": "",
        "status": "PENDING"
    }

    response = requests.post(
        BASE_URL,
        json=invalid_delivery
    )

    assert response.status_code == 400


def test_create_delivery_with_blank_status():

    invalid_delivery = {
        "customerName": "Test Customer",
        "address": "50 Test Street",
        "postcode": "M3 1AA",
        "status": ""
    }

    response = requests.post(
        BASE_URL,
        json=invalid_delivery
    )

    assert response.status_code == 400