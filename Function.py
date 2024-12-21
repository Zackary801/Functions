def display_menu():
    """Displays the food menu with prices."""
    menu = {
        1: ("Burger", 5.99),
        2: ("Pizza", 8.99),
        3: ("Sandwich", 4.99),
        4: ("Pasta", 7.49),
        5: ("Salad", 6.49)
    }
    print("\n--- Food Menu ---")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - ${value[1]:.2f}")
    return menu

def get_user_selection(menu):
    """Prompts the user to select a menu item."""
    while True:
        try:
            choice = int(input("\nEnter the number of the item you want to order: "))
            if choice in menu:
                return menu[choice]
            else:
                print("Invalid choice. Please select a valid menu item.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_payment(total_cost):
    """Handles the payment process."""
    while True:
        try:
            cash = float(input(f"The total is ${total_cost:.2f}. Enter cash amount: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment accepted. Your change is ${change:.2f}.")
                break
            else:
                print(f"Insufficient funds. You need ${total_cost - cash:.2f} more.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    """Main function to run the food ordering system."""
    menu = display_menu()
    selected_item = get_user_selection(menu)
    print(f"\nYou selected: {selected_item[0]} - ${selected_item[1]:.2f}")
    process_payment(selected_item[1])
    print("\nThank you for your order!")

if __name__ == "__main__":
    main()
