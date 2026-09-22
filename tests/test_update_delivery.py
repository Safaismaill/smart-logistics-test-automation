import requests

from config import BASE_URL


def test_update_delivery():

    # First create a temporary delivery to update
    new_delivery = {
        "customerName": "Update Test Customer",
        "address": "10 Original Street",
        "postcode": "M4 1AA",
        "status": "PENDING"
    }

    create_response = requests.post(
        BASE_URL,
        json=new_delivery
    )

    assert create_response.status_code == 200

    created_delivery = create_response.json()
    delivery_id = created_delivery["id"]

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

    # Clean up the temporary record
    delete_response = requests.delete(
        f"{BASE_URL}/{delivery_id}"
    )

    assert delete_response.status_code == 200


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

    # API should return 404 Not Found
    assert response.status_code == 404

    error_response = response.json()

    assert error_response["error"] == "Delivery with ID 999 was not found"


def test_update_delivery_with_blank_status():

    # Create a temporary delivery first
    new_delivery = {
        "customerName": "Validation Test Customer",
        "address": "30 Test Street",
        "postcode": "M7 1AA",
        "status": "PENDING"
    }

    create_response = requests.post(
        BASE_URL,
        json=new_delivery
    )

    assert create_response.status_code == 200

    created_delivery = create_response.json()
    delivery_id = created_delivery["id"]

    # Try to update it with invalid data
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

    # Clean up the temporary delivery
    delete_response = requests.delete(
        f"{BASE_URL}/{delivery_id}"
    )

    assert delete_response.status_code == 200