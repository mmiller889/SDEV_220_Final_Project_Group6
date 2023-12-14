import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self, inventory):
        super().__init__()
        self.title("Ordering System")
        self.geometry("600x500")
        self.inventory = inventory

        tk.Label(self, text="Place Your Order", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="In-Store Pickup", command=self.in_store_pickup).pack(pady=5)
        tk.Button(self, text="Shipping", command=self.shipping).pack(pady=5)
        tk.Button(self, text="Exit", command=self.quit).pack(pady=5)

        self.load_and_display_image("warehousse.png", (143, 113), (10, 10))
        self.load_and_display_image("thankyu.png", (143, 113), (450, 10))

    def load_and_display_image(self, image_path, size, position):
        canvas = tk.Canvas(self, width=size[0], height=size[1])
        canvas.place(x=position[0], y=position[1])

        try:
            image = Image.open(image_path)
            image = image.resize(size)
            photo_image = ImageTk.PhotoImage(image)
            canvas.create_image(size[0] // 2, size[1] // 2, image=photo_image)
            canvas.image = photo_image
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image file {image_path} not found.")

    def in_store_pickup(self):
        messagebox.showinfo("Order", "In-Store Pickup selected. Choose items in the next window.")

    def shipping(self):
        messagebox.showinfo("Order", "Shipping selected. Choose items in the next window.")

if __name__ == "__main__":
    root = MainWindow({})
    root.mainloop()
