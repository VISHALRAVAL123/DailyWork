import tkinter as tk
from tkinter import messagebox

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class InvoiceItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        return self.product.price * self.quantity


class Invoice:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_amount(self):
        total = 0
        for item in self.items:
            total += item.get_total()
        return total


def add_item_to_invoice():
    product_name = product_entry.get()
    quantity = int(quantity_entry.get())

    # Find the product from the products list
    product = None
    for p in products:
        if p.name == product_name:
            product = p
            break

    if product is None:
        messagebox.showerror("Error", "Product not found.")
        return

    # Create an invoice item and add it to the invoice
    item = InvoiceItem(product, quantity)
    invoice.add_item(item)

    # Update the total amount label
    total_amount = invoice.get_total_amount()
    total_amount_label.config(text=f"Total Amount: ${total_amount}")

    # Clear the entry fields
    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


# Create some products
products = [
    Product("Product 1", 10),
    Product("Product 2", 15),
    Product("Product 3", 20)
]

# Create an invoice
invoice = Invoice()

# Create the main Tkinter window
window = tk.Tk()
window.title("Billing Software")

# Create labels and entry fields for product and quantity
product_label = tk.Label(window, text="Product:")
product_label.pack()
product_entry = tk.Entry(window)
product_entry.pack()

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

# Create a button to add items to the invoice
add_button = tk.Button(window, text="Add Item", command=add_item_to_invoice)
add_button.pack()

# Create a label to display the total amount
total_amount_label = tk.Label(window, text="Total Amount: $0")
total_amount_label.pack()

window.mainloop()
