# Smart Logistics API Test Automation

A Python automated testing project created to test the Smart Logistics & Delivery Management REST API.

The project uses Pytest and Requests to test the main API functionality including retrieving, creating, updating, deleting and filtering delivery records.

## Technologies Used

- Python
- Pytest
- Requests
- REST APIs
- Git
- GitHub

## Features Tested

The automated test suite currently covers:

- Retrieve all deliveries
- Retrieve a delivery by ID
- Check JSON response structure
- Handle missing delivery IDs
- Create new deliveries
- Validate required fields when creating deliveries
- Update existing deliveries
- Validate incorrect update data
- Delete deliveries
- Confirm deleted deliveries can no longer be retrieved
- Filter deliveries by status
- Filter deliveries by postcode
- Search by customer name
- Use multiple filters together

## Test Coverage

The project currently contains 18 automated API tests covering successful requests and error scenarios.

The tests check:

- HTTP status codes
- JSON response data
- Required fields
- Validation errors
- 404 Not Found responses
- Search and filtering
- CRUD operations

## Project Structure

```text
smart-logistics-test-automation/
│
├── tests/
│   ├── conftest.py
│   ├── test_create_delivery.py
│   ├── test_delete_delivery.py
│   ├── test_filters.py
│   ├── test_get_deliveries.py
│   └── test_update_delivery.py
│
├── config.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md