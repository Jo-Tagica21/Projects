# Shopping cart

from datetime import datetime

class ShoppingItems:
    '''
    Shopping Items attributes
    '''
    def __init__(self):
        self.items = []

    def retrieve_items(self):
        '''
        Retrieve items from text file and append to list
        '''
        # Clear list for each retrieval
        self.items.clear()
        # Open file to read items
        with open('shopping_items.txt', 'r', encoding='utf-8') as file:
            # split content from file to access the item and its price
            for line in file:
                item_info = line.strip().split(';')
                # Add items from the text file to list
                self.items.append(item_info)
        return self.items

    def display_items(self):
        '''
        Display available items
        '''
        # iterate through list displaying product and its price
        for i, item in enumerate(self.items,1):
            product, price = item
            print(f"{i}   - {product}: £{price}")

class ShoppingCart(ShoppingItems):
    '''
    Shopping Cart attributes
    '''
    def __init__(self):
        super().__init__()
        self.basket = []

    def add_item(self):
        '''
        Add item to basket
        '''
        user_option = int(input("\nEnter item corresponding number: "))
        # add item to basket
        if 0 < user_option <= len(self.items):
            selected_item = self.items[user_option-1]
            # Check if the item is already in the basket
            found = False
            for basket_item in self.basket:
                if basket_item['item'] == selected_item:
                    # Increment quantity if item is found
                    basket_item['quantity'] += 1
                    found = True
                    break
            # Add item as new entry
            if not found:
                self.basket.append({'item': selected_item, 'quantity': 1})
        else:
            print("Invalid entry.")
    def remove_item(self):
        '''
        Remove item from basket
        '''
        user_option = int(input("\nEnter item corresponding number: "))
        # remove item from basket based on user input
        if 0 <= user_option <= len(self.basket):
            self.basket.remove(self.basket[user_option-1])
        else:
            print("Invalid entry.")

    def display_basket(self):
        '''
        Display items in basket
        '''
        for i, basket_item in enumerate(self.basket, 1):
            product, price = basket_item['item']
            quantity = basket_item['quantity']
            print(f"{i}   - {product}: £{price} x{quantity}")

    def calculate_total(self):
        '''
        Calculte total basket items
        '''
        total_price = 0.0
        for item in self.basket:
            # Convert price from string to float and multiply by quantity
            price = float(item['item'][1])
            total_price += price * item['quantity']
        print(f"\n\tTotal: £{total_price:.2f}")
        return total_price

    def create_receipt(self):
        '''
        Append a new receipt with a timestamp as its unique identifier.
        '''
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open('customer_receipt.txt', 'a', encoding='utf-8') as receipt_file:
            # Timestamp for each new receipt
            receipt_file.write(f'\nReceipt - {timestamp}\n')
            for basket_item in self.basket:
                product, price = basket_item['item']
                quantity = basket_item['quantity']
                # Write purchased items to file
                receipt_file.write(f"{product} - £{price} x{quantity}\n")
                
            # Calculate and write total price
            total_price = self.calculate_total()
            # Write total price to the file
            receipt_file.write(f"Total: £{total_price:.2f}\n")


cart = ShoppingCart()

print("\nWelcome To jt's Shopping Cart Interface")

while True:
    print("""
[1]: Add item
[2]: Remove item
[3]: View shopping basket
[4]: Checkout
""")
    user_choice = (input("Select an option: "))
    if user_choice == '1':
        cart.retrieve_items()
        cart.display_items()
        cart.add_item()

    elif user_choice == '2':
        print("\nBasket: ")
        cart.display_basket()
        cart.remove_item()

    elif user_choice == '3':
        print("\nBasket: ")
        cart.display_basket()
        cart.calculate_total()
        print("""
[1]: Continue shopping
[2]: Checkout
""")
        user_decision = input("Would you like to continue or checkout: ")
        if user_decision == '1':
            continue
        if user_decision == '2':
            cart.create_receipt()
            break

    elif user_choice == '4':
        cart.create_receipt()
        print("Thank you for shopping with us. Goodbye")
        break

    else:
        print("Invalid entry")
        continue            