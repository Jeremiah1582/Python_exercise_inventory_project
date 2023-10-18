products = ["Laptop", "Mobile Phone", "Television", "Refrigerator", "Microwave", "Washing Machine", "Blender"]
# option 1
def display_product_positions():
    print("\n Displaying Products with Positions:")
    for position, product in enumerate(products, start=1):
        print(f"{product} - {position}")
# option 2
def check_product_position():
    product_name = input("\nEnter the name of the product to find its position: ").strip()
    for position, product in enumerate(products):
        if product.lower() == product_name.lower():
            print(f"{product_name} is at position {position+1}.")
            break
    else:
        print("Product not found.")
# option 3
def display_products_in_range():
    start_pos = int(input("\nEnter the starting position: "))
    end_pos = int(input("Enter the ending position: "))

    if start_pos < 1 or end_pos > len(products) or start_pos > end_pos:
        print("Invalid range. Please enter a valid range next time.")
        return

    print("\nProducts within the specified range:")
    for position, product in enumerate(products[start_pos-1:end_pos], start=start_pos):
        print(f"{product} - {position}")

# Option Menu 
while True:
    print("\n--- Inventory Management ---")
    print("1. Display products with positions.")
    print("2. Check product position.")
    print("3. Display products within a range.")
    print("4. Exit.")
    
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        display_product_positions()
    elif choice == '2':
        check_product_position()
    elif choice == '3':
        display_products_in_range()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# This solution provides an interactive way to:

# 1. Display all products with their positions.
# 2. Check a specific product's position.
# 3. Display products within a specified range.

# The program continues to loop until the user decides to exit. 
# The `enumerate()` function is used in conjunction with the `start` parameter to display positions starting from 1, even though list indices start at 0.