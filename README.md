🧾 Sixty4bitSquad Invoice Generator
Welcome to the Sixty4bitSquad Invoice Generator! 🎉 This Python script helps you easily create beautiful, professional invoices in PDF format. With just a few details about your customer and the items or services they purchased, you’ll have an invoice ready in no time!

💡 How It Works
1. 📦 Installation
➡First, you'll need to install the dependencies to run this script. Make sure you have Python installed, then run:

pip install fpdf

This will install the FPDF library that is used to create the PDF invoices.

3. 🚀 Features
➡Add a logo to the invoice 🖼️
➡Customize currency (USD or INR) 💸
➡Add multiple items with their quantity and price 🛒
➡Automatic total calculation 🔢
➡Generates a clean and professional PDF invoice 📄

4. 🔍 Code Explanation
Let’s break down how this code works:

➡Imports & Setup: import datetime
from fpdf import FPDF

We import the datetime module to handle dates 🗓️.
We import FPDF, a library that helps create PDFs with Python 📄.
➡Custom Class for the Invoice: class Sixty4bitSquadInvoiceMaker(FPDF):
➡We create a custom class Sixty4bitSquadInvoiceMaker by extending the FPDF class. This helps us define how our invoices will look 💻.
➡Adding Fonts: self.add_font('Montserrat', '', 'Montserrat-Regular.ttf', uni=True)
self.add_font('Montserrat', 'B', 'Montserrat-Bold.ttf', uni=True)

➡We’re adding two fonts here: regular and bold versions of Montserrat, a clean and professional font ✍️.
➡Header:

def header(self):
    self.set_fill_color(20, 20, 20)  
    self.rect(0, 0, 210, 297, 'F')
    self.image('logo.png', x=(210-100)/2, y=20, w=100)
    
➡The header includes a background color for the entire page and adds a logo at the top center. The logo.png image is placed if it’s available 🖼️.
If the logo is missing, you can skip it (you could add error handling for that).

➡Footer:

def footer(self):
    self.set_y(-20)
    self.set_font('Montserrat', '', 10)
    self.set_text_color(200, 200, 200)
    self.cell(0, 10, 'Thank You For Your Purchase', 0, 0, 'C')
    
➡The footer adds a "Thank You" message at the bottom of each invoice. This helps maintain a friendly tone 😊.
Creating the Invoice:


def create_invoice(self, invoice_number, date, customer_name, email, items):

This function is where the magic happens! 💫
It accepts the invoice number, date, customer name, email, and a list of items (products or services).
➡We calculate the total price for each item and sum them up to show the subtotal and final total 💰.

➡Main Function:

def main():
➡This function runs everything. It asks for user input (invoice number, customer details, items, etc.) and then creates the invoice 🎯.
You can add as many items as you need and print out the final invoice in PDF format.


➡Save as PDF:

filename = f"invoice_{invoice_number}.pdf"
invoice.output(filename)
print(f"Invoice generated: {filename}")
The invoice is saved as a PDF file named using the invoice number, so it’s easy to find and organize 📂.


4. 🛠️ How to Use It
➡Run the script using Python:

python invoice_generator.py
The script will ask for details like:

Currency (USD/INR)
Invoice number and date
Customer name and email
Items (description, quantity, and price)
After entering the information, the script will generate a PDF invoice in the current folder with the name format invoice_<invoice_number>.pdf 📄.

5. 📝 Notes
➡You can customize the logo by placing a logo.png file in the same folder as the script. If the logo file is not present, you can handle this with a try-except block to skip it.
The date can be auto-filled if you don't want to enter it manually.

7. 🌟 Example Invoice
➡Here’s how a typical invoice will look:

Customer name and email at the top 🧑‍💼
List of items with their price and quantity 🛍️
Total calculated automatically at the bottom 💵

▀▀█▀▀ █──█ █▀▀█ █▀▀▄ █─█ 　 
─░█── █▀▀█ █▄▄█ █──█ █▀▄ 　 
─░█── ▀──▀ ▀──▀ ▀──▀ ▀─▀ 　 

█──█ █▀▀█ █──█ 
█▄▄█ █──█ █──█ 
▄▄▄█ ▀▀▀▀ ─▀▀▀
            
