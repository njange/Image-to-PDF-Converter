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
        title_label = tk.Label(self.root, text = "Image to PDF Converter", font = ("Arial", 20, "bold"))
        title_label.pack(pady = 10)

def main():
    root = tk.Tk()
    root.title("Image to PDF Converter")
    root.geometry("400x600")
    app = ImagetoPDFConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()


