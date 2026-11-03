def fetch_product(product_id):
    raise NotImplementedError("Replace with an HTTP client implementation")


def get_product_name(product_id):
    product = fetch_product(product_id)
    title = product.get("title")
    if not title:
        raise ValueError("Product title is missing")
    return title