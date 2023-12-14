import tkinter as tk
from tkinter import messagebox, simpledialog
from OrderSystem import OrderWindow

class ClothingInventory(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clothing Inventory System")
        self.geometry("500x400")

        self.inventory = {
            "Jeans": 1600,
            "Sweaters": 1200,
            "V-Neck Tops": 1400,
            "Long-Sleeve Tops": 400
        }

        tk.Label(self, text="Clothing Inventory System", font=("Arial", 16)).pack(pady=10)

        self.inventory_listbox = tk.Listbox(self)
        self.inventory_listbox.pack(pady=10, expand=True, fill='both')
        self.update_inventory_listbox()

        tk.Button(self, text="Update Inventory", command=self.open_update_window).pack(pady=5)
        tk.Button(self, text="Launch Ordering System", command=self.launch_ordering_system).pack(pady=5)

    def update_inventory_listbox(self):
        self.inventory_listbox.delete(0, tk.END)
        for item, quantity in self.inventory.items():
            self.inventory_listbox.insert(tk.END, f"{item}: {quantity}")

    def open_update_window(self):
        product = simpledialog.askstring("Update Inventory", "Enter product name:")
        if product not in self.inventory:
            messagebox.showerror("Error", "Product not found.")
            return
        quantity = simpledialog.askinteger("Update Inventory", "Enter new quantity:")
        if quantity is None or quantity < 0:
            messagebox.showerror("Error", "Invalid quantity.")
            return
        self.inventory[product] = quantity
        self.update_inventory_listbox()

    def launch_ordering_system(self):
        OrderWindow(self.inventory).mainloop()

if __name__ == "__main__":
    root = ClothingInventory()
    root.mainloop()
