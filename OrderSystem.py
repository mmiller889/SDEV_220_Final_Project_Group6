import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class OrderWindow(tk.Toplevel):
    def __init__(self, master, orders, **kwargs):
        super().__init__(master, **kwargs)
        # Set the title and size of the order management window
        self.title("Order Management System")
        self.geometry("700x500")

        # Store the list of orders passed from the parent window
        self.orders = orders

        # Create the widgets for the GUI
        self.create_widgets()

    def create_widgets(self):
        # Configure the style for the treeview
        self.style = ttk.Style(self)
        self.style.configure('Treeview', rowheight=25)

        # Create a frame to hold other widgets
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=10, pady=10, expand=True, fill='both')

        # Title label for the window
        self.label = ttk.Label(self.frame, text="Manage Orders", font=("Arial", 16))
        self.label.pack(pady=10)

        # Treeview for displaying orders
        self.order_tree = ttk.Treeview(self.frame, columns=('OrderID', 'Product', 'Quantity'), show='headings')
        self.order_tree.heading('OrderID', text='Order ID')
        self.order_tree.heading('Product', text='Product')
        self.order_tree.heading('Quantity', text='Quantity')
        self.order_tree.pack(pady=10, expand=True, fill='both')

        # Update the treeview with the current orders
        self.update_order_treeview()

        # Buttons for viewing and editing orders
        self.view_order_btn = ttk.Button(self.frame, text="View Orders", command=self.view_orders)
        self.view_order_btn.pack(side=tk.LEFT, padx=10)

        self.edit_order_btn = ttk.Button(self.frame, text="Edit Orders", command=self.edit_orders)
        self.edit_order_btn.pack(side=tk.RIGHT, padx=10)

    def update_order_treeview(self):
        # Clear the treeview and update it with the current orders
        for i in self.order_tree.get_children():
            self.order_tree.delete(i)
        for order in self.orders:
            self.order_tree.insert('', tk.END, values=(order['id'], order['product'], order['quantity']))

    def view_orders(self):
        # Currently, this method does not have a specific implementation
        pass

    def edit_orders(self):
        # Edit the quantity of a selected order in the treeview
        selected_item = self.order_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No order selected.")
            return

        new_quantity = simpledialog.askinteger("Edit Order", "Enter new quantity:", parent=self)
        if new_quantity is not None and new_quantity >= 0:
            order_id = self.order_tree.item(selected_item)['values'][0]
            # Find and update the quantity of the selected order
            for order in self.orders:
                if order['id'] == order_id:
                    order['quantity'] = new_quantity
                    break
            # Refresh the treeview to reflect the updated order
            self.update_order_treeview()
        else:
            messagebox.showerror("Error", "Invalid quantity.", parent=self)
