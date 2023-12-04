import tkinter as tk
from tkinter import messagebox

class ClothingInventory(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1000, height=1000)
        self.title("Clothing Inventory System")

        # Inventory with initial quantities
        self.inventory = {
            "Jeans": 1600,
            "Sweaters": 1200,
            "V-Neck Tops": 1400,
            "Long-Sleeve Tops": 400
        }

        # Create a label
        label1 = tk.Label(self, text="Welcome to Our Clothing Inventory System")
        label1.pack()
        
        # Create a button that displays inventory
        button_view_inventory = tk.Button(self, text="View Inventory", command=self.display_inventory)
        button_view_inventory.pack()
        
        # Create a button that opens a window to update inventory
        button_update_inventory = tk.Button(self, text="Update Inventory", command=self.open_update_window)
        button_update_inventory.pack()

    def display_inventory(self):
        # Display inventory details
        inventory_details = "\n".join(f"{item}: {quantity}" for item, quantity in self.inventory.items())
        messagebox.showinfo("Inventory Details", inventory_details)

    def open_update_window(self):
        # Create a window to update inventory (Add, Remove, Update products)
        update_window = tk.Toplevel()
        update_window.title("Update Inventory")

        # Labels and entry fields to add, remove, or update products
        product_label = tk.Label(update_window, text="Product Name:")
        product_label.pack()
        product_entry = tk.Entry(update_window)
        product_entry.pack()

        quantity_label = tk.Label(update_window, text="Quantity:")
        quantity_label.pack()
        quantity_entry = tk.Entry(update_window)
        quantity_entry.pack()

        # Buttons to add, remove, or update products
        add_button = tk.Button(update_window, text="Add Product", command=lambda: self.update_inventory(product_entry.get(), int(quantity_entry.get())))
        add_button.pack()

    def update_inventory(self, product, quantity):
        # Update inventory based on user input
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity
        messagebox.showinfo("Inventory Updated", f"{product} quantity updated to {self.inventory[product]}")

# Initialize the Clothing Inventory System
root = ClothingInventory()
root.mainloop()
