import csv
from fooditems import *
from inventory import *
from datetime import datetime


def load_inventory(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, category, quantity, barcode, expiry_date = row
                    food_item = FoodItem(name, category, int(quantity), barcode, datetime.datetime.strptime(expiry_date, '%Y-%m-%d').date())
                    self.food_items.append(food_item)
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty inventory.")
        except Exception as e:
            print(f"Error in inventory file: {e}")

def save_inventory(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                for item in self.food_items:
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date])
        except Exception as e:
            print(f"Error saving inventory: {e}")