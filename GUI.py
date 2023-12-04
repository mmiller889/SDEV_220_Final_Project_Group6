import tkinter as tk
from tkinter import messagebox

class ClothingInventory(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=500, height=300)  # Adjusted window size for consistency
        self.title("Clothing Inventory System")

        # Inventory with initial quantities
        self.inventory = {
            "Jeans": 1600,
            "Sweaters": 1200,
            "V-Neck Tops": 1400,
            "Long-Sleeve Tops": 400
        }

        # Welcome label
        label1 = tk.Label(self, text="Welcome to Our Clothing Inventory System")
        label1.pack()
        
        # Button to display inventory
        button_view_inventory = tk.Button(self, text="View Inventory", command=self.display_inventory)
        button_view_inventory.pack()
        
        # Button to open update window
        button_update_inventory = tk.Button(self, text="Update Inventory", command=self.open_update_window)
        button_update_inventory.pack()

    def display_inventory(self):
        # Display current inventory in a message box
        inventory_details = "\n".join(f"{item}: {quantity}" for item, quantity in self.inventory.items())
        messagebox.showinfo("Inventory Details", inventory_details)

    def open_update_window(self):
        # Window for updating inventory items
        update_window = tk.Toplevel(self)
        update_window.title("Update Inventory")
        update_window.geometry("400x200")  # Consistent window size

        # Product name input
        product_label = tk.Label(update_window, text="Product Name:")
        product_label.pack()
        self.product_entry = tk.Entry(update_window)
        self.product_entry.pack()

        # Quantity input
        quantity_label = tk.Label(update_window, text="Quantity:")
        quantity_label.pack()
        self.quantity_entry = tk.Entry(update_window)
        self.quantity_entry.pack()

        # Button to add or update product
        add_button = tk.Button(update_window, text="Add/Update Product", 
                               command=self.update_inventory)
        add_button.pack()

    def update_inventory(self):
        # Update inventory after validating input
        product = self.product_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            self.inventory[product] = self.inventory.get(product, 0) + quantity
            messagebox.showinfo("Inventory Updated", 
                                f"{product} quantity updated to {self.inventory[product]}")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

# Initialize and run the Clothing Inventory System
if __name__ == "__main__":
    root = ClothingInventory()
    root.mainloop()
