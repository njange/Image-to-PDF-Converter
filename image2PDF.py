import tkinter as tk
from tkinter import filedialog
import os

class ImagetoPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_image_listbox = tk.Listbox(root, selectmode = tk.MULTIPLE)
        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text = "Image to PDF Converter",font = ("Arial", 20, "bold"))
        title_label.pack(pady = 10)

        select_image_button = tk.Button(self.root, text = "Select Images", command = self.select_images)
        select_image_button.pack(pady =(0,10))

        self.selected_image_listbox.pack(pady = (0,10), fill=tk.BOTH, expand = True)

        label = tk.Label(self.root, text = "Enter output PDF Name" )
        label.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable = self.output_pdf_name, width=40, justify="center")
        pdf_name_entry.pack()

        convert_button = tk.Button(self.root, text = "Convert to PDF", command = self.convert_to_pdf)
        convert_button.pack(pady = (20,40))

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(title = "Select Images", filetypes = (("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("All Files", "*.*")))

    def convert_to_pdf(self):
        # Define the functionality for converting images to PDF here
        pass

def main():
    root = tk.Tk()
    root.title("Image to PDF Converter")
    root.geometry("400x600")
    app = ImagetoPDFConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()



