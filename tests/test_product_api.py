"""
Hodaya Shirazie
21390778-5
"""


import pytest
import requests

BASE_URL = "https://dummyjson.com"


@pytest.mark.parametrize(
    "product_id",
    [
        pytest.param(1, id="first-product"),
        pytest.param(2, id="second-product"),
        pytest.param(3, id="third-product"),
    ],
)
def test_get_product_by_id(product_id):
    # TODO 1: Send a GET request to /products/{product_id}
    response = requests.get(f"{BASE_URL}/products/{product_id}")

    # TODO 2: Assert that the status code is 200
    assert response.status_code == 200

    # TODO 3: Parse the JSON response
    product = response.json()

    # TODO 4: Assert that the returned ID matches product_id
    assert product["id"] == product_id

    # TODO 5: Assert that the response contains a title and price
    assert "title" in product
    assert "price" in product


@pytest.mark.parametrize(
    "search_term",
    [
        pytest.param("phone", id="search-phone"),
        pytest.param("laptop", id="search-laptop"),
    ],
)




def test_search_products(search_term):
    # TODO 1: Send GET /products/search with q=search_term
    response = requests.get(f"{BASE_URL}/products/search", params={"q": search_term})

    # TODO 2: Assert status code
    assert response.status_code == 200

    # TODO 3: Parse the JSON response and check its structure
    data = response.json()

    assert "products" in data
    assert isinstance(data["products"], list)
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    # TODO 4: Verify the search behavior
    for product in data["products"]:
        searchable_text = (product["title"] + " " + product.get("description", "")).lower()
        assert search_term.lower() in searchable_text


@pytest.mark.parametrize(
    "limit",
    [
        pytest.param(1, id="one-result"),
        pytest.param(5, id="five-results"),
    ],
)



def test_product_limit(limit):
    # TODO: Send GET /products with the limit query parameter
    response = requests.get(f"{BASE_URL}/products", params={"limit": limit})

    data = response.json()

    # TODO: Assert status code
    assert response.status_code == 200

    # TODO: Assert len(response["products"]) <= limit
    assert len(data["products"]) <= limit

    # TODO: Check the response pagination metadata
    assert data["limit"] == limit
    