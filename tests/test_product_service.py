import pytest
import product_service as serviceHodaya


def test_product_title(monkeypatch):
    def mock_fetch_product(product_id):
        return {"title": "Test Product"}

    monkeypatch.setattr(serviceHodaya, "fetch_product", mock_fetch_product)
    assert serviceHodaya.get_product_name(1) == "Test Product"


def test_missing_title(monkeypatch):
    def mock_fetch_product(product_id):
        return {"id": "1"}

    monkeypatch.setattr(serviceHodaya, "fetch_product", mock_fetch_product)

    with pytest.raises(ValueError, match="Product title is missing"):
        serviceHodaya.get_product_name(1)



def test_dependency_timeout(monkeypatch):
    def mock_fetch_product(product_id):
        raise TimeoutError("Request timed out")

    monkeypatch.setattr(serviceHodaya, "fetch_product", mock_fetch_product)

    with pytest.raises(TimeoutError, match="Request timed out"):
        serviceHodaya.get_product_name(1)


def test_dependency_called_with_requested_id(monkeypatch):
    called_ids = []

    def mock_fetch_product(product_id):
        called_ids.append(product_id)
        return {"title": "Test Product"}

    monkeypatch.setattr(serviceHodaya, "fetch_product", mock_fetch_product)

    serviceHodaya.get_product_name(123)

    assert called_ids == [123]
