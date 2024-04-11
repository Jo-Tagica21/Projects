# Admin controls to edit available shopping items

'''
USERNAME: admin
PASSWORD: password
'''

class ShoppingItems:
    '''
    Add a new item attritbutes
    '''
    def __init__(self):
        self.item = []

    def retrieve_items(self):
        '''
        Retrive items from textfile and append to list
        '''
        self.item.clear()
        with open('shopping_items.txt', 'r', encoding='utf-8') as file:
            for line in file:
                item_info = line.strip().split(';')
                self.item.append(item_info)

    def display_items(self):
        '''
        Display available items
        '''
        # iterate through list displaying product and its price
        for i, item in enumerate(self.item,1):
            product, price = item
            print(f"{i}   - {product}: £{price}")

    def add_item(self):
        '''
        Adding a new item to texfile
        '''
        self.retrieve_items()
        max_length = max((len(item[0]) for item in self.item), default=0)
        while True:
            new_item = input("Enter new item: ")
            if len(new_item) <= 3:
                print("Item name too short")
                continue
            item_price = input("Enter price: ")

            # Calculate spaces to add to match longest product name
            # Organisation and displya purposes
            spaces_to_add = max_length - len(new_item)
            if spaces_to_add > 0:
                adjusted_item_name = new_item + (' ' * spaces_to_add)
            else:
                adjusted_item_name = new_item

            with open('shopping_items.txt', 'a', encoding='utf-8') as file:
                file.write(f"{adjusted_item_name};{item_price}\n")

            print(f"'{new_item}' added successfully.")
            break

    def remove_item(self):
        '''
        Remove an item chosen by the user from the text file
        '''
        item_number = int(input("Enter the item number to remove: "))
        # Check if input number is within the range of available items
        if 1 <= item_number <= len(self.item):
            # Remove the selected item
            removed_item = self.item.pop(item_number - 1)
            print(f"Removed item: {removed_item[0]}")
            
            # Rewrite to file without removed item
            with open('shopping_items.txt', 'w', encoding='utf-8') as file:
                for item in self.item:
                    file.write(';'.join(item) + '\n')
        else:
            print("Invalid entry")

cart = ShoppingItems()

# Login module
logged_in = False
while not logged_in:
    print("\nLOGIN")
    Admin_user = input("Username: ")
    Admin_Pass = input("Password: ")
    
    # lower function applied to anticipate case sensitive error
    if Admin_user.lower() != "admin":
        print("User does not exist")
        continue
    if Admin_Pass.lower() != "password":
        print("Wrong password")
        continue
    
    print("Login Successful!")
    logged_in = True

# Menu interaction
while True:
    menu_options = print("""
[1]: Add a new item
[2]: Remove an item
[3]: Exit
""")
    menu_choice = input("Select an option: ")
    if menu_choice == '1':
        cart.add_item()
    if menu_choice == '2':
        cart.retrieve_items()
        cart.display_items()
        cart.remove_item()
        
    if menu_choice == '3':
        print("Goodbye")
        break


