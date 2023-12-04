import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1000, height=1000)
        self.title("Clothing Inventory")

        # Create a label
        label1 = tk.Label(self, text="Ordering!")
        label1.pack()
        
        # Create a button that opens a secondary window
        button1 = tk.Button(self, text="Start Order for In-Store Pickup", command=self.open_secondary_window)
        button1.pack()
        
        # Create a button that opens a secondary window
        button2 = tk.Button(self, text="Start Order for shipping", command=self.open_secondary_window)
        button2.pack()

        # Create a button that exits the application
        button3 = tk.Button(self, text="Exit", command=self.quit)
        button3.pack()

        #Create Canvas
        canvas= Canvas(self, width=143, height=113)
        canvas.pack()
        
        # Create a photoimage object of the image in the path
        image1 = Image.open("warehousse.png")
        image1 = image1.resize((100,100))
        self.ph = ImageTk.PhotoImage(image1)
        
        
        #Add image to the Canvas Items
        canvas.create_image(100,100,image=self.ph)

        #Create Canvas
        canvas= Canvas(self, width=143, height=113)
        canvas.pack()
        
        # Create a photoimage object of the image in the path
        image2 = Image.open("thankyu.png")
        image2 = image2.resize((100,100))
        self.ph2 = ImageTk.PhotoImage(image2)
       
        
        #Add image to the Canvas Items
        canvas.create_image(100,100,image=self.ph2)

    def open_secondary_window(self):
        # Create secondary (or popup) window.
        newWindow = tk.Toplevel()
        newWindow.title("Avaliable Clothes")
        newWindow.config(width=10, height=10)

        # Create input labels and entry boxes
        self.Long_Jeanslbl = tk.Label(newWindow, text="Long Jeans ($15.00)")
        self.Long_Jeans_ent = tk.Entry(newWindow)
        self.Skinny_Jeans_lbl = tk.Label(newWindow, text="Skinny Jeans ($15.00)")
        self.Skinny_Jeans_ent = tk.Entry(newWindow)
        self.Tshirt_lbl = tk.Label(newWindow, text="Tshirt ($15.00)")
        self.Tshirt_ent = tk.Entry(newWindow)
        self.Long_Sleeve_Shirt_lbl = tk.Label(newWindow, text="Long Sleeve Shirt($17.00)")
        self.Long_Sleeve_Shirt_ent = tk.Entry(newWindow)
        self.Sweater_lbl = tk.Label(newWindow, text="Sweater ($17.00)")
        self.Sweater_ent = tk.Entry(newWindow)
        self.Crew_Neck_lbl = tk.Label(newWindow, text="Crew Neck ($17.00)")
        self.Crew_Neck_ent = tk.Entry(newWindow)
