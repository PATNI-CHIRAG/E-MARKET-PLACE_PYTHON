class Billing_Purchase:
    def __init__(self, product_name, brand, price, quantity, user_name, contact):
        self.product_name = product_name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.user_name = user_name
        self.contact = contact

    def generate_bill(self, payment_method):
        total_cost = self.price * self.quantity  # This must be a number
        print("\n================== BILL ==================")
        print(f"Customer Name: {self.user_name}")
        print(f"Contact: {self.contact}")
        print(f"Product: {self.product_name} ({self.brand})")
        print(f"Quantity: {self.quantity}")
        print(f"Price per unit: ${self.price}")
        print(f"Total Cost: ${total_cost}")
        print(f"Payment Method: {payment_method}")
        print("===========================================")

class Billing_Cart_purchase:
    def __init__(self, user_name, contact):
        self.user_name = user_name
        self.contact = contact
        self.cart_items = []

    def add_item(self, product_name, price, quantity):
        total_item_price = price * quantity
        self.cart_items.append({
            "product_name": product_name,
            "price": price,
            "quantity": quantity,
            "total_item_price": total_item_price
        })

    def generate_consolidated_bill(self, payment_method):
        total_cost = 0
        print("\nYour Purchase Bill:")
        print("--------------------------------------------------")
        print("Product Name | Quantity | Price | Total Price")
        print("--------------------------------------------------")
        
        # Print individual items
        for item in self.cart_items:
            total_cost += item["total_item_price"]
            print(f"{item['product_name']} | {item['quantity']} | ${item['price']} | ${item['total_item_price']}")

        print("--------------------------------------------------")
        print(f"Total Price: ${total_cost}")
        print("\nProduct purchase successful! Generating consolidated bill...")

        # Generate bill with payment method
        print("\n================== CONSOLIDATED BILL ==================")
        print(f"Customer Name: {self.user_name}")
        print(f"Contact: {self.contact}")
        bill_price = 0
        for item in self.cart_items:
            print(f"Product: {item['product_name']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Price per unit: ${item['price']}")
            print(f"Total Cost: ${item['total_item_price']}")
            bill_price+=item['total_item_price']
        print(f"Payment Method: {payment_method}")
        print(f"Total Bill Price: {bill_price}")
        print("===========================================")

    def clear_cart(self):
        self.cart_items.clear()