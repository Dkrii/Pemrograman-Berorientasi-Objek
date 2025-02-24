class CartItem:
    def __init__(self, item_name, price, quantity=1):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def add_item(self, quantity):
        self.quantity += quantity
        return f"Added {quantity} more of '{self.item_name}'. Total quantity: {self.quantity}"

    def remove_item(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            return f"Removed {quantity} of '{self.item_name}'. Remaining quantity: {self.quantity}"
        else:
            return f"Cannot remove {quantity} of '{self.item_name}'. Only {self.quantity} available."

    def calculate_total(self):
        return self.price * self.quantity

    def show_info(self):
        return f"Item: {self.item_name}, Price: ${self.price}, Quantity: {self.quantity}, Total: ${self.calculate_total()}"

# Creating a cart item
item1 = CartItem("Laptop", 1000, 2)
print(item1.add_item(1))  
print(item1.remove_item(1))  
print(item1.show_info())  

cart_items = []

while True:
    print("Menu")
    print("1. List cart items")
    print("2. Add item to cart")
    print("3. Add quantity to existing item")
    print("4. Remove quantity from existing item")
    print("5. Exit")

    menu = input("Select menu: ")
    if menu == "1":
        for index, item in enumerate(cart_items):
            print(f"{index} - {item.show_info()}")

    elif menu == "2":
        item_name = input("Insert item name: ")
        price = float(input("Insert price: "))
        quantity = int(input("Insert quantity: "))
        new_item = CartItem(item_name, price, quantity)
        cart_items.append(new_item)

    elif menu == "3":
        index = int(input("Choose item index: "))
        quantity = int(input("Insert quantity to add: "))
        print(cart_items[index].add_item(quantity))

    elif menu == "4":
        index = int(input("Choose item index: "))
        quantity = int(input("Insert quantity to remove: "))
        print(cart_items[index].remove_item(quantity))

    elif menu == "5":
        break