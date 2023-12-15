import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from OrderEntry import OrderEntry

class ClothingInventory(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set the title and size of the main window
        self.title("Clothing Inventory System")
        self.geometry("600x450")

        # Create the widgets for the GUI
        self.create_widgets()

        # Initialize the inventory data
        self.init_inventory()

    def create_widgets(self):
        # Configure the style for the treeview
        self.style = ttk.Style(self)
        self.style.configure('Treeview', rowheight=25)

        # Create a frame to hold the other widgets
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=10, pady=10, expand=True, fill='both')

        # Title label
        self.label = ttk.Label(self.frame, text="Clothing Inventory System", font=("Arial", 16))
        self.label.pack(pady=10)

        # Treeview for displaying inventory
        self.tree = ttk.Treeview(self.frame, columns=('Product', 'Quantity'), show='headings')
        self.tree.heading('Product', text='Product')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.column('Product', width=200)
        self.tree.column('Quantity', width=100, anchor=tk.CENTER)
        self.tree.pack(pady=10, expand=True, fill='both')

        # Buttons for updating inventory and launching the order system
        self.update_btn = ttk.Button(self.frame, text="Update Inventory", command=self.open_update_window)
        self.update_btn.pack(side=tk.LEFT, padx=10)

        self.order_btn = ttk.Button(self.frame, text="Launch Ordering System", command=self.launch_ordering_system)
        self.order_btn.pack(side=tk.RIGHT, padx=10)

    def init_inventory(self):
        # Initialize the inventory with some default values
        self.inventory = {
            "Jeans": 1600,
            "Sweaters": 1200,
            "V-Neck Tops": 1400,
            "Long-Sleeve Tops": 400
        }
        # Update the treeview with these inventory values
        self.update_inventory_treeview()

    def update_inventory_treeview(self):
        # Clear the treeview and update it with the current inventory
        for i in self.tree.get_children():
            self.tree.delete(i)
        for item, quantity in self.inventory.items():
            self.tree.insert('', tk.END, values=(item, quantity))

    def open_update_window(self):
        # Open a dialog to update the inventory
        product = simpledialog.askstring("Update Inventory", "Enter product name:", parent=self)
        if product and product not in self.inventory:
            messagebox.showerror("Error", "Product not found.", parent=self)
            return
        quantity = simpledialog.askinteger("Update Inventory", "Enter new quantity:", parent=self)
        if quantity is not None and quantity >= 0:
            self.inventory[product] = quantity
            self.update_inventory_treeview()
        else:
            messagebox.showerror("Error", "Invalid quantity.", parent=self)

    def launch_ordering_system(self):
        # Launch the order entry system, passing the current inventory
        OrderEntry(self.inventory)
    
if __name__ == "__main__":
    # Instantiate and run the main application window
    root = ClothingInventory()
    root.mainloop()
