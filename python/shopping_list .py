shopping_list = []

def add():
    pro = str(input("Enter the name of the product you want to add: "))
    shopping_list.append(pro)
    print("The product has been added.")

def delete():
    d = str(input("Please enter the product you want to remove: "))
    if d in shopping_list:
        shopping_list.remove(d)
        print("The product has been removed.")
    else:
        print("This product does not exist in the shopping list.")

def show():
    if shopping_list:
        print("Shopping list:")
        for product in shopping_list:
            print(f"- {product}")
    else:
        print("The shopping list is empty.")

print("Hello to shopping_list!")
while True:
    ask = str(input("What do you want to do? (add, remove, show, or end): ")).lower()
    if ask == "add":
        add()
    elif ask == "remove":
        delete()
    elif ask == "show":
        show()
    elif ask == "end":
        break
    else:
        print("Invalid input. Please enter 'add', 'remove', 'show', or 'end'.")
    
    l = str(input("Do you want to do anything else? (yes/no): ")).lower()
    if l == "no":
        break
    elif l != "yes":
        print("Invalid input. Exiting the program.")
        break
