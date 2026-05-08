from csv import DictReader
from io import TextIOWrapper

from shopapp.models import Product, Order


def save_csv_products(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)

    products = [
        Product(**row)
        for row in reader
    ]
    Product.objects.bulk_create(products)
    return products


def save_csv_orders(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)

    orders = []
    for row in reader:
        products_ids_str = row.pop("products", "")
        order = Order.objects.create(**row)

        if products_ids_str:
            products_ids = [pk.strip() for pk in products_ids_str.split(",")]
            products = Product.objects.filter(id__in=products_ids)
            order.products.set(products)
        orders.append(order)

    return orders