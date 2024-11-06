import os
restaurants = [{"name":"Sushi", "category":"Japanese", "status": False},
               {"name":"Burguer", "category":"Fast-Food","status": True},
               {"name":"Pasta", "category":"Italian", "status": False}] 

def display_program_name():
    print ("𝙱𝚒𝚜𝚝𝚛𝚘𝙱𝚘𝚡")

def display_options():
    print ("1. List restaurants")
    print ("2. Register a new restaurant")
    print ("3. Update restaurant status")
    print ("4. Exit")

def chosen_option():

    try:
        option_chosen = int(input("Choose an option: "))
        if option_chosen == 1:
            list_restaurants()
        elif option_chosen == 2:
            register_restaurant()
        elif option_chosen == 3:
            update_restaurant_status()
        elif option_chosen == 4:
            print("Goodbye")
        else:
            invalid_option()
    except ValueError:
        invalid_option()  

def list_restaurants():
    display_subtitle("List restaurants\n")

    print (f"{"Restaurant name".ljust(20)} | {"Category".ljust(20)} | {"Status"}")
    for restaurant in restaurants:
        restaurant_name = restaurant["name"]
        category = restaurant["category"]    
        status = "Activated" if restaurant["status"] else "Deactivated"

        print (f"{restaurant_name.ljust(20)} | {category.ljust(20)} | {status}")

    return_to_main_menu()

def register_restaurant():
    display_subtitle("Register a new restaurant")
    restaurant_name = input(f"Enter the name of the restaurant: ")
    category = input(f"Enter the category of the restaurant {restaurant_name}: ")
    restaurant_data = {"name": restaurant_name, "category": category, "status": True}
    restaurants.append(restaurant_data)
    print(f"The restaurant {restaurant_name} has been successfully registered!")
    return_to_main_menu()
    main()

def update_restaurant_status():
    display_subtitle("Update restaurant status")
    restaurant_name = input("Enter the name of the restaurant: ")
    restaurants_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant["name"]:
            restaurants_found = True
            restaurant["status"] = not restaurant["status"]
            status= "Activated" if restaurant["status"] else "Deactivated"
            print(f"The status of the restaurant {restaurant_name} has been successfully updated to {status}")
    if not restaurants_found:
        print("Restaurant not found")
    return_to_main_menu()

def invalid_option():
    print ("Invalid option\n")
    return_to_main_menu()

def display_subtitle(text):
    os.system("cls")
    line= "*" * (len(text))
    print (line)
    print (text)
    print (line)
    print()

def return_to_main_menu():
    input("Press any key to return to the main menu:")
    main()

def exit_program():
    display_subtitle("Goodbye")

def main():
    os.system("cls")
    display_program_name()
    display_options()
    chosen_option()
    exit_program()

if __name__ == "__main__":
    main()