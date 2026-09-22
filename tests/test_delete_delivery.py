import requests

from config import BASE_URL

def test_delete_delivery():

    # Create a temporary delivery that we can safely delete
    new_delivery = {
        "customerName": "Delete Test Customer",
        "address": "40 Delete Street",
        "postcode": "M8 1AA",
        "status": "PENDING"
    }

    create_response = requests.post(
        BASE_URL,
        json=new_delivery
    )

    assert create_response.status_code == 200

    created_delivery = create_response.json()
    delivery_id = created_delivery["id"]

    # Delete the temporary delivery
    delete_response = requests.delete(
        f"{BASE_URL}/{delivery_id}"
    )

    assert delete_response.status_code == 200

    # Try to retrieve the deleted delivery
    get_response = requests.get(
        f"{BASE_URL}/{delivery_id}"
    )

    # It should no longer exist
    assert get_response.status_code == 404


def test_delete_delivery_that_does_not_exist():

    # Try to delete an ID that does not exist
    response = requests.delete(
        f"{BASE_URL}/999"
    )

    # API should return 404 Not Found
    assert response.status_code == 404

    error_response = response.json()

    assert error_response["error"] == "Delivery with ID 999 was not found"