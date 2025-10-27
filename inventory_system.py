"""
Inventory Management System
---------------------------
This module manages a simple inventory with functionality to:
- Add and remove items
- Load and save data to JSON
- Log operations safely
- Check low stock items
"""

import json
import logging
from datetime import datetime
import ast


# Configure logging once
logging.basicConfig(
    filename='inventory_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def add_item(stock_data, item="default", qty=0, logs=None):
    """Add an item with quantity to the stock."""
    if logs is None:
        logs = []

    # Validate input types
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning(
            "Invalid input types for add_item: item=%s, qty=%s", item, qty
        )
        return stock_data

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %s of %s", qty, item)
    return stock_data


def remove_item(stock_data, item, qty):
    """Remove a quantity of an item from stock safely."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
                logging.info("Removed %s completely from stock", item)
        else:
            logging.warning("Attempted to remove non-existent item: %s", item)
    except KeyError as err:
        logging.error("KeyError while removing item: %s", err)
    return stock_data


def get_qty(stock_data, item):
    """Return quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a file."""
    stock_data = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.loads(file.read())
        logging.info("Data loaded from %s", file_path)
    except FileNotFoundError:
        logging.warning(
            "%s not found, starting with empty inventory", file_path
        )
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON from %s", file_path)
    return stock_data


def save_data(stock_data, file_path="inventory.json"):
    """Save inventory data to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(json.dumps(stock_data, indent=4))
    logging.info("Data saved to %s", file_path)


def print_data(stock_data):
    """Print all inventory items and quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Return list of items with stock below threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main program to demonstrate inventory system."""
    stock_data = {}

    stock_data = add_item(stock_data, "apple", 10)
    stock_data = add_item(stock_data, "banana", 5)
    stock_data = add_item(stock_data, 123, "ten")  # invalid types logged
    stock_data = remove_item(stock_data, "apple", 3)
    stock_data = remove_item(stock_data, "orange", 1)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")

    save_data(stock_data)
    stock_data = load_data()

    print_data(stock_data)

    # Safe evaluation example
    code = "['safe', 'test']"
    safe_result = ast.literal_eval(code)
    print("Literal eval result:", safe_result)


if __name__ == "__main__":
    main()
