import requests

from config import BASE_URL


def test_update_delivery(create_delivery):

    # Create a temporary delivery using the reusable fixture
    delivery = create_delivery(
        customer_name="Update Test Customer",
        address="10 Original Street",
        postcode="M4 1AA",
        status="PENDING"
    )

    delivery_id = delivery["id"]

    # New values we want to save
    updated_delivery = {
        "customerName": "Updated Customer",
        "address": "20 Updated Street",
        "postcode": "M5 2BB",
        "status": "DELIVERED"
    }

    # Send PUT request to update the delivery
    update_response = requests.put(
        f"{BASE_URL}/{delivery_id}",
        json=updated_delivery
    )

    assert update_response.status_code == 200

    result = update_response.json()

    # Check that the values were updated
    assert result["id"] == delivery_id
    assert result["customerName"] == "Updated Customer"
    assert result["address"] == "20 Updated Street"
    assert result["postcode"] == "M5 2BB"
    assert result["status"] == "DELIVERED"


def test_update_delivery_that_does_not_exist():

    updated_delivery = {
        "customerName": "Missing Customer",
        "address": "10 Test Street",
        "postcode": "M6 1AA",
        "status": "PENDING"
    }

    # Try to update a delivery ID that does not exist
    response = requests.put(
        f"{BASE_URL}/999",
        json=updated_delivery
    )

    assert response.status_code == 404

    error_response = response.json()

    assert error_response["error"] == "Delivery with ID 999 was not found"


def test_update_delivery_with_blank_status(create_delivery):

    # Create a temporary delivery using the fixture
    delivery = create_delivery(
        customer_name="Validation Test Customer",
        address="30 Test Street",
        postcode="M7 1AA",
        status="PENDING"
    )

    delivery_id = delivery["id"]

    # Try to update the delivery with a blank status
    invalid_update = {
        "customerName": "Validation Test Customer",
        "address": "30 Test Street",
        "postcode": "M7 1AA",
        "status": ""
    }

    update_response = requests.put(
        f"{BASE_URL}/{delivery_id}",
        json=invalid_update
    )

    # Blank status should fail validation
    assert update_response.status_code == 400