import pytest
import requests

from config import BASE_URL


@pytest.fixture
def create_delivery():

    # Store IDs created during a test
    created_delivery_ids = []

    def _create_delivery(
        customer_name="Test Customer",
        address="50 Test Street",
        postcode="M3 1AA",
        status="PENDING"
    ):

        delivery_data = {
            "customerName": customer_name,
            "address": address,
            "postcode": postcode,
            "status": status
        }

        response = requests.post(
            BASE_URL,
            json=delivery_data
        )

        assert response.status_code == 200

        delivery = response.json()

        # Remember the ID so it can be cleaned up later
        created_delivery_ids.append(delivery["id"])

        return delivery

    # Give the helper function to the test
    yield _create_delivery

    # Automatically clean up deliveries after the test
    for delivery_id in created_delivery_ids:

        response = requests.delete(
            f"{BASE_URL}/{delivery_id}"
        )

        # 404 is also acceptable if the test already deleted it
        assert response.status_code in [200, 404]