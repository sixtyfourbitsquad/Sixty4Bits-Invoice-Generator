import datetime
from fpdf import FPDF

class Sixty4bitSquadInvoiceMaker(FPDF):
    def __init__(self, currency):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.add_font('Montserrat', '', 'Montserrat-Regular.ttf', uni=True)
        self.add_font('Montserrat', 'B', 'Montserrat-Bold.ttf', uni=True)
        self.currency = currency

    def header(self):
        self.set_fill_color(20, 20, 20)  # Dark background
        self.rect(0, 0, 210, 297, 'F')
        
        # Center the logo
        self.image('logo.png', x=(210-100)/2, y=20, w=100)  # Adjust w=100 to change logo size
        self.ln(50)  # Space after logo

    def footer(self):
        self.set_y(-20)
        self.set_font('Montserrat', '', 10)
        self.set_text_color(200, 200, 200)
        self.cell(0, 10, 'Thank You For Your Purchase', 0, 0, 'C')

    def create_invoice(self, invoice_number, date, customer_name, email, items):
        self.add_page()
        self.set_font('Montserrat', '', 12)
        self.set_text_color(200, 200, 200)

        # Invoice details
        self.cell(100, 10, 'Invoice to:', 0, 0)
        self.cell(0, 10, f'Invoice No. {invoice_number}', 0, 1, 'R')
        self.cell(100, 10, customer_name, 0, 0)
        self.cell(0, 10, date, 0, 1, 'R')
        self.cell(0, 10, email, 0, 1, 'R')
        self.ln(20)

        # Table header
        self.set_font('Montserrat', 'B', 12)
        self.set_text_color(255, 215, 0)  # Golden color for headers
        self.cell(90, 10, 'Item', 0, 0)
        self.cell(30, 10, 'Price', 0, 0)
        self.cell(30, 10, 'Qty', 0, 0)
        self.cell(40, 10, 'Total', 0, 1)

        # Table contents
        self.set_font('Montserrat', '', 12)
        self.set_text_color(200, 200, 200)
        total = 0
        for item in items:
            self.cell(90, 10, item['description'], 0, 0)
            self.cell(30, 10, f"{self.currency} {item['price']:.2f}", 0, 0)
            self.cell(30, 10, str(item['quantity']), 0, 0)
            item_total = item['quantity'] * item['price']
            self.cell(40, 10, f"{self.currency} {item_total:.2f}", 0, 1)
            total += item_total

        # Separator line
        self.ln(5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(10)

        # Totals
        self.cell(150, 10, 'Sub-total', 0, 0, 'R')
        self.cell(40, 10, f"{self.currency} {total:.2f}", 0, 1, 'R')
        self.cell(150, 10, 'Tax', 0, 0, 'R')
        self.cell(40, 10, f"{self.currency} 0.00", 0, 1, 'R')
        self.set_font('Montserrat', 'B', 12)
        self.cell(150, 10, 'Total', 0, 0, 'R')
        self.cell(40, 10, f"{self.currency} {total:.2f}", 0, 1, 'R')

        self.ln(20)
        self.set_font('Montserrat', '', 10)
        self.multi_cell(0, 5, "*Please make the payment to the details\nwhich are provided to you personally.", 0, 'L')

def main():
    print("Sixty4bitSquad Invoice Generator")
    print("--------------------------------")
    
    # Currency selection
    while True:
        currency = input("Choose currency (USD/INR): ").upper()
        if currency in ['USD', 'INR']:
            break
        print("Invalid choice. Please enter USD or INR.")
    
    invoice = Sixty4bitSquadInvoiceMaker(currency)
    
    invoice_number = input("Enter invoice number: ")
    date = input("Enter invoice date (e.g., March 20, 2030): ")
    customer_name = input("Enter customer name: ")
    email = input("Enter email: ")
    
    items = []
    while True:
        item = {
            'description': input("Enter item description: "),
            'quantity': int(input("Enter quantity: ")),
            'price': float(input(f"Enter price in {currency}: "))
        }
        items.append(item)
        if input("Add another item? (y/n): ").lower() != 'y':
            break
    
    invoice.create_invoice(invoice_number, date, customer_name, email, items)
    filename = f"invoice_{invoice_number}.pdf"
    invoice.output(filename)
    print(f"Invoice generated: {filename}")

if __name__ == "__main__":
    main()