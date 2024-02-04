# SOLE SHOPPER PROJECT:

items = []

def main():
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")

    if len(phone_number) != 10:
        print("Please enter a 10-digit phone number.")
        return

    try:
        phone_number = int(phone_number)
    except ValueError:
        print("Please enter a valid numeric phone number.")
        return

    age = input("Enter your age: ")

    if len(age) != 2:
        print("Please enter a 2-digit age.")
        return

    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid numeric age.")
        return

    address = input("Enter your address: ")

    print(f"\nWelcome, {name}!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            shop()
        elif choice == "2":
            display_items()
        elif choice == "3":
            delete_from_cart()
        elif choice == "4":
            generate_bill()
        elif choice == "5":
            print("Thank you for shopping with us! see you soon :))")
            break
        else:
            print("Invalid choice!")

def display_menu():
    print("\n===== Welcome to SOLE SHOPPER =====/")
    print("1. Shop")
    print("2. Add to Cart")
    print("3. Delete from Cart")
    print("4. Generate Bill")
    print("5. Quit")

def shop():
    print("\n===== Available Shoes =====/")
    print("1. Nike")
    print("2. Adidas")
    print("3. Puma")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        shop_nike()
    elif choice == "2":
        shop_adidas()
    elif choice == "3":
        shop_puma()
    else:
        print("Invalid choice!")
        return

def shop_nike():
    print("\n===== Nike Shoes =====/")
    print("1. Nike Air Force 1  - ₹9695")
    print("2. Nike Air Max 97 - ₹16995")
    print("3. Nike Dunk High Retro Premium - ₹11495")

    shoe_choice = input("Enter your choice (1-3): ")

    if shoe_choice == "1":
        item = "Nike Air Force 1"
        price = 9695
    elif shoe_choice == "2":
        item = "Nike Air Max 97"
        price = 16995
    elif shoe_choice == "3":
        item = "Nike Dunk High Retro Premium "
        price = 11495
    else:
        print("Invalid choice!")
        return

    items.append({"item": item, "price": price})
    print(f"Added {item} to cart.")

def shop_adidas():
    print("\n===== Adidas Shoes =====/")
    print("1. SUPERSTAR SHOES - ₹8999")
    print("2. WEB BOOST SHOES - ₹10499")
    print("3. Adidas Stan Smith - ₹11999")

    shoe_choice = input("Enter your choice (1-2): ")

    if shoe_choice == "1":
        item = "SUPERSTAR SHOES"
        price = 8999
    elif shoe_choice == "2":
        item = "WEB BOOST SHOES"
        price = 10499
    elif shoe_choice == "3":
        item = "Adidas Stan Smith"
        price = 11999
    else:
        print("Invalid choice!")
        return

    items.append({"item": item, "price": price})
    print(f"Added {item} to cart.")

def shop_puma():
    print("\n===== Puma Shoes =====/")
    print("1. RS-X GEN.G PUMA Unisex Sneakers - ₹5499")
    print("2. PUMA x KOCHE Plexus Mid Unisex Sneakers - ₹12799")
    print("3. Rider Future Vintage Unisex Sneakers - ₹7199")

    shoe_choice = input("Enter your choice (1-2): ")

    if shoe_choice == "1":
        item = "RS-X GEN.G PUMA Unisex Sneakers"
        price = 5499
    elif shoe_choice == "2":
        item = "PUMA x KOCHE Plexus Mid Unisex Sneakers"
        price = 12799
    elif shoe_choice == "3":
        item = "Rider Future Vintage Unisex Sneakers"
        price = 7199
    else:
        print("Invalid choice!")
        return

    items.append({"item": item, "price": price})
    print(f"Added {item} to cart.")

def display_items():
    if not items:
        print("Your cart is empty.")
    else:
        print("\n===== Cart Contents =====/")
        for item in items:
            print(f"{item['item']} - ₹{item['price']}")

def delete_from_cart():
    display_items()

    if not items:
        print("Your cart is empty.")
        return

    choice = input("Enter the item number to delete (1-{}): ".format(len(items)))

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(items):
            item = items.pop(choice - 1)
            print("Deleted {} from cart.".format(item['item']))
        else:
            print("Invalid item number!")
    else:
        print("Invalid input!")

def generate_bill():
    if not items:
        print("Your cart is empty. Nothing to bill.")
        return

    print("\n===== Bill =====/")
    total_cost = sum(item['price'] for item in items)

    for item in items:
        print(f"{item['item']}: ₹{item['price']}")

    print("---------------")
    print(f"Total: ₹{total_cost}")

    proceed_payment = input("Do you want to proceed with the payment? (yes/no): ")

    if proceed_payment.lower() == "yes":
        upi_id = input("Enter your UPI ID: ")
        make_payment(total_cost, upi_id)
        items.clear()
    else:
        print("Payment cancelled.")

def make_payment(amount, upi_id):
    print(f"Payment of ₹{amount} through UPI ID {upi_id} successful. Thank you for shopping with us!")

main()
