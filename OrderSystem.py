import tkinter as tk
from tkinter import messagebox

class OrderWindow(tk.Tk):
    def __init__(self, inventory):
        super().__init__()
        self.title("Order System")
        self.geometry("500x400")
        self.inventory = inventory

        tk.Label(self, text="Place Your Order", font=("Arial", 16)).pack(pady=10)

        self.order_listbox = tk.Listbox(self)
        self.order_listbox.pack(pady=10, expand=True, fill='both')
        self.update_order_listbox()

        tk.Button(self, text="Place Order", command=self.place_order).pack(pady=5)

    def update_order_listbox(self):
        self.order_listbox.delete(0, tk.END)
        for item, quantity in self.inventory.items():
            if quantity > 0:
                self.order_listbox.insert(tk.END, item)

    def place_order(self):
        selection = self.order_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "No item selected.")
            return
        item = self.order_listbox.get(selection)
        self.inventory[item] -= 1  # Decrement inventory
        messagebox.showinfo("Order Placed", f"Order placed for {item}.")
        self.update_order_listbox()

if __name__ == "__main__":
    root = OrderWindow({})
    root.mainloop()
