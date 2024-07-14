# fooditems.py

import datetime

class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = expiry_date

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Barcode: {self.barcode}, Expiry Date: {self.expiry_date}"
