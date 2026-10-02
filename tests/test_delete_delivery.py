import requests

from config import BASE_URL


def test_delete_delivery(create_delivery):

    # Create a temporary delivery using the reusable fixture
    delivery = create_delivery(
        customer_name="Delete Test Customer",
        address="40 Delete Street",
        postcode="M8 1AA",
        status="PENDING"
    )

    delivery_id = delivery["id"]

    # Delete the temporary delivery
    delete_response = requests.delete(
        f"{BASE_URL}/{delivery_id}"
    )

    assert delete_response.status_code == 200

    # Try to retrieve the deleted delivery
    get_response = requests.get(
        f"{BASE_URL}/{delivery_id}"
    )

    # The delivery should no longer exist
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