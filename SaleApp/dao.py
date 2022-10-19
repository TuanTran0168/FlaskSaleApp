import json
from SaleApp import app

def load_categories():
    with open("%s/data/categories.json" % app.root_path, encoding="utf-8") as file:
        return json.load(file)


def load_products():
    with open("%s/data/products.json" % app.root_path, encoding="utf-8") as file:
        return json.load(file)

