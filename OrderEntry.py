import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from OrderSystem import OrderWindow

class OrderEntry(tk.Tk):
    def __init__(self, inventory):
        super().__init__()
        # Set the title and size of the order entry window
        self.title("Order Entry System")
        self.geometry("600x450")

        # Store the inventory passed from the parent window
        self.inventory = inventory

        # Create the widgets for the GUI
        self.create_widgets()

        # Initialize a list to store orders and an ID counter for new orders
        self.orders = []
        self.order_id = 1

    def create_widgets(self):
        # Configure the style for the treeview
        self.style = ttk.Style(self)
        self.style.configure('Treeview', rowheight=25)

        # Create a frame to hold other widgets
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=10, pady=10, expand=True, fill='both')

        # Title label for the window
        self.label = ttk.Label(self.frame, text="Place an Order", font=("Arial", 16))
        self.label.pack(pady=10)

        # Dropdown to select the item for the order
        self.item_label = ttk.Label(self.frame, text="Select Item:")
        self.item_label.pack(pady=5)
        self.item_combobox = ttk.Combobox(self.frame, values=list(self.inventory.keys()))
        self.item_combobox.pack(pady=5)

        # Entry field for order quantity
        self.quantity_label = ttk.Label(self.frame, text="Enter Quantity:")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = ttk.Entry(self.frame)
        self.quantity_entry.pack(pady=5)

        # Button to place the order
        self.order_btn = ttk.Button(self.frame, text="Place Order", command=self.place_order)
        self.order_btn.pack(pady=10)

        # Button to manage orders
        self.manage_orders_btn = ttk.Button(self.frame, text="Manage Orders", command=self.launch_order_management)
        self.manage_orders_btn.pack(pady=10)

    def place_order(self):
        # Logic to place an order and update the inventory
        item = self.item_combobox.get()
        try:
            quantity = int(self.quantity_entry.get())
            if item not in self.inventory or quantity <= 0 or self.inventory[item] < quantity:
                raise ValueError
            # Subtract the ordered quantity from the inventory
            self.inventory[item] -= quantity

            # Create a new order and add it to the orders list
            order = {'id': self.order_id, 'product': item, 'quantity': quantity}
            self.orders.append(order)
            self.order_id += 1

            messagebox.showinfo("Order Placed", f"Order for {quantity} {item}(s) placed successfully.")
        except ValueError:
            messagebox.showerror("Order Error", "Invalid item or quantity.")

    def launch_order_management(self):
        # Open the OrderWindow with the current orders for management
        OrderWindow(self, self.orders)

if __name__ == "__main__":
    # Example inventory data to start the application with
    inventory = {"Jeans": 1600, "Sweaters": 1200, "V-Neck Tops": 1400, "Long-Sleeve Tops": 400}
    root = OrderEntry(inventory)
    root.mainloop()
