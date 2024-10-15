import tkinter as tk
from tkinter import messagebox

# Define the products data in dictionaries
m_dict = {
    'redmi': {'Brand Name': ' Redmi', 'Model Name': ' Note 13 Pro', 'Product ID': ' MR001', 'Price     ': ' 14999',
              'Discount  ': ' 5%'},
    'oppo': {'Brand Name': ' Oppo', 'Model Name': ' Reno 15 Pro', 'Product ID': ' MO001', 'Price     ': ' 21499',
             'Discount  ': ' 7%'},
    'vivo': {'Brand Name': ' Vivo', 'Model Name': ' Y12 Plus', 'Product ID': ' MV001', 'Price     ': ' 20000',
             'Discount  ': ' 8%'},
    'apple': {'Brand Name': ' Apple', 'Model Name': ' 15 Pro Max', 'Product ID': ' MA001', 'Price     ': ' 121499',
              'Discount  ': ' 7%'}}

w_dict = {'sonata': {'Brand Name': ' Sonata', 'Model Name': ' RMP-3', 'Product ID': ' SW001', 'Price     ': ' 25499',
                     'Discount  ': ' 5%'},
          'fastrack': {'Brand Name': ' Fastrack', 'Model Name': ' QM01y', 'Product ID': ' FW001', 'Price     ': ' 5600',
                       'Discount  ': ' 7%'},
          'titan': {'Brand Name': ' Titan', 'Model Name': ' 9011SL', 'Product ID': ' TW001', 'Price     ': ' 11450',
                    'Discount  ': ' 8%'},
          'rolex': {'Brand Name': ' Rolex', 'Model Name': ' GMT-Mster', 'Product ID': ' RW001',
                    'Price     ': ' 1833000', 'Discount  ': ' 7%'}}


# GUI Application
class ZodioMartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zodio Mart")
        self.root.geometry("600x400")

        # Welcome Message
        welcome_label = tk.Label(root, text="Welcome to Zodio Mart", font=("Arial", 16))
        welcome_label.pack(pady=10)

        # Product Selection
        self.product_label = tk.Label(root, text="Pick a Product Category:")
        self.product_label.pack()

        self.product_var = tk.StringVar()
        self.product_menu = tk.OptionMenu(root, self.product_var, "Mobiles", "Watches", "TV", "Laptops")
        self.product_menu.pack(pady=10)

        # Button to select product
        self.product_button = tk.Button(root, text="Select", command=self.select_product)
        self.product_button.pack(pady=10)

    def select_product(self):
        product = self.product_var.get().lower()

        if product == 'mobiles':
            self.show_mobile_options()
        elif product == 'watches':
            self.show_watch_options()
        else:
            messagebox.showinfo("Notice", f"{product.capitalize()} not available yet in the demo.")

    def show_mobile_options(self):
        self.new_window("Mobiles", m_dict)

    def show_watch_options(self):
        self.new_window("Watches", w_dict)

    def new_window(self, title, product_dict):
        new_window = tk.Toplevel(self.root)
        new_window.title(title)
        new_window.geometry("500x400")

        label = tk.Label(new_window, text=f"Select {title}: ")
        label.pack(pady=10)

        self.product_var = tk.StringVar(new_window)
        options = list(product_dict.keys())
        self.product_menu = tk.OptionMenu(new_window, self.product_var, *options)
        self.product_menu.pack(pady=10)

        button = tk.Button(new_window, text="Select",
                           command=lambda: self.show_product_details(product_dict))
        button.pack(pady=10)

    def show_product_details(self, product_dict):
        selected_product = self.product_var.get().lower()

        if selected_product in product_dict:
            details = product_dict[selected_product]
            messagebox.showinfo("Product Details",
                                f"Brand: {details['Brand Name']}\n"
                                f"Model: {details['Model Name']}\n"
                                f"Price: {details['Price     ']}\n"
                                f"Discount: {details['Discount  ']}")


# Main Application
root = tk.Tk()
app = ZodioMartApp(root)
root.mainloop()
