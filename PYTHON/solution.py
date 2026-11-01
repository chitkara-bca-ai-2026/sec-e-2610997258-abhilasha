# Lab 13 - Inventory Control System
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]
while True:
    print("\n==========================================")
    print("         INVENTORY CONTROL SYSTEM         ")
    print("==========================================")
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    print("==========================================")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        print("\n--- Current Inventory ---")
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            for idx, item in enumerate(inventory, 1):
                print(f"{idx}. {item}")
    elif choice == 2:
        new_item = input("Enter item name to add: ")
        inventory.append(new_item)
        print(f"[SUCCESS] \"{new_item}\" added to inventory.")
    elif choice == 3:
        item_to_remove = input("Enter item name to remove: ")
        if item_to_remove in inventory:
            inventory.remove(item_to_remove)
            print(f"[SUCCESS] \"{item_to_remove}\" removed from inventory.")
        else:
            print(f"[ERROR] \"{item_to_remove}\" not found in inventory.")
    elif choice == 4:
        inventory.sort()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("\n--- Current Inventory ---")
        for idx, item in enumerate(inventory, 1):
            print(f"{idx}. {item}")
    elif choice == 5:
        print("\nThank you for using Inventory Control System. Goodbye!")
        break
    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 5.")