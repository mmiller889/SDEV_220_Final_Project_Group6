import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=500, height=300)  # Adjusted window size for consistency
        self.title("Clothing Inventory")

        # Main label
        label1 = tk.Label(self, text="Ordering!")
        label1.pack()
        
        # Buttons for different types of orders
        button1 = tk.Button(self, text="Start Order for In-Store Pickup", 
                            command=lambda: self.open_secondary_window("In-Store Pickup"))
        button1.pack()
        
        button2 = tk.Button(self, text="Start Order for Shipping", 
                            command=lambda: self.open_secondary_window("Shipping"))
        button2.pack()

        # Exit button
        button3 = tk.Button(self, text="Exit", command=self.quit)
        button3.pack()

        # Load and display images
        self.load_and_display_image("warehousse.png", 1)
        self.load_and_display_image("thankyu.png", 2)

    def load_and_display_image(self, image_path, canvas_num):
        # Function to load and display an image in a canvas
        canvas = tk.Canvas(self, width=143, height=113)
        canvas.pack()

        image = Image.open(image_path)
        image = image.resize((100,100))
        photo_image = ImageTk.PhotoImage(image)
        canvas.create_image(100, 100, image=photo_image)
        setattr(self, f"photo_image_{canvas_num}", photo_image)  # Prevent garbage collection

    def open_secondary_window(self, order_type):
        # Create secondary window for order placement
        newWindow = tk.Toplevel(self)
        newWindow.title(f"Available Clothes - {order_type}")
        newWindow.geometry("400x600")  # Consistent window size

        # Code for creating order form goes here (not included for brevity)

# Running the main application loop
if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
