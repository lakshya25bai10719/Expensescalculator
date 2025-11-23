import os

FILE_NAME = "expenses.txt"

def add_expense():
    print("\n--- ADD NEW EXPENSE ---")
    
    date = input("Enter Date (YYYY-MM-DD): ")

    category = input("Enter Category (Food, Travel, Bills, etc.): ")
    
    amount = float(input("Enter Amount: "))
    
    description = input("Enter Short Description: ")

    record = f"{date},{category},{amount},{description}\n"

    with open(FILE_NAME, "a") as file:
        file.write(record)
        print("Success: Expense saved!")


def view_expenses():
    print("\n--- YOUR EXPENSE HISTORY ---")
    
    if not os.path.exists(FILE_NAME):
        print("No records found. Try adding an expense first.")
        return

    with open(FILE_NAME, "r") as file:
        print("Date \t Category \t Amount \t Description")
        print("-" * 50)
        
        # Iterating directly over the file object (the normal way)
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                date, category, amount, desc = parts
                
                print(f"{date} \t {category} \t {amount} \t {desc}")

def calculate_total():
    print("\n--- TOTAL SPENDING ---")
    
    if not os.path.exists(FILE_NAME):
        print("No data to calculate.")
        return

    total = 0.0
    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            # Basic check to avoid crashing on empty lines
            if len(parts) >= 3:
                total += float(parts[2])
        
        print(f"Total amount spent so far: {total}")

def main_menu():
    while True:
        print("\n==========================")
        print(" PERSONAL EXPENSE TRACKER ")
        print("==========================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            print("Exiting... Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()