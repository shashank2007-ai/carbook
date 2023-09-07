
import datetime
def main():
    time = datetime.datetime.now()
    print("""     
                   _______
                  //  ||\ \\
            _____//___||_\ \___
            )  _          _    \\
            |_/ \________/ \___|
           ___\_/________\_/______
       """)
 
    print("\n\tWELCOME TO CAR BOOKING SYSTEM!\n")
    print(f"\tCurrent date and time: {time}")
 
    while True:
        print("""
        ******** Car Booking System ********
        1. Admin
        2. Unregistered Customer
        3. Registered Customer
        4. Exit the program
        """)
 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            admin()
 
        elif choice == 2:
            unregistered_function()
 
        elif choice == 3:
            registered_function()
 
        elif choice == 4:
            break
        
        else:
            print("Please enter a choice between 1-4 only!")
 
 
def login(user, password, elevated):
    with open("User_Data.txt" if not elevated else "Admin_Data.txt", "r") as text:
        print("%s Login ********" % ("******** Admin" if elevated else "******** User"))
        for record in text:
            recordList = record.rstrip().split(":")
            if user.lower() in recordList[0].lower() and password in recordList[1]:
                print("Welcome, %s" % user)
                return True
        print("Error! Wrong username or password")
        return False
 
 
def admin():
    nValue = input("Enter username: ")
    pValue = input("Enter password: ")
    if login(nValue, pValue, True):
        admin_function()
 
 
def admin_function():
    while True:
        print("""
            ******** Access System ********
            1. Add Car with details, to be rented out
            2. Modify Car Details
            3. Display All records of
                a. Cars available for Rent
                b. Customer Payment for a specific time duration
            4. Search Specific record of
                a. Specific Car Booking
                b. Specific Customer Payment
            5. Return a Rented car
            6. Exit to main menu
            """)
 
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            add_cars()
 
        elif choice == 2:
            modify_cars()
 
        elif choice == 3:
            option = input("option a or b? ")
            if option == 'a':
                display_cars()
            else:
                print("Customers Payment for a specific time duration")  # customers_payment function goes here
 
        elif choice == 4:
            option = input("option a or b?")
            if option == 'a':
                print("Specific Search of Car Booking")  # search_car_booking of function goes here
            else:
                print("Specific Search of Customer Payment")  # search_customer_pay function goes here
 
        elif choice == 5:
            print("return_cars()")
 
        elif choice == 6:
            break
 
        else:
            print("Please enter a number between 1-6 only!")
 
 
def get_new_users():
    with open("User_Data.txt", "a") as text:
        while True:
            name = input("Enter name to register: ")
            password = input("Enter password: ")
            record = name + ":" + password
            text.write(record + "\n")
            break
 
 
def existing_users():
    nValue = input("Username: ")
    pValue = input("Password: ")
    return login(nValue, pValue, False)
 
 
def display_cars():
    with open("DisplayCars_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.rstrip().split(":")
            car_type = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            print("%d. Type: %s Brand: %s Color: %s Year: %s" % (index, car_type, brand, color, year))
            index += 1
 
 
def add_cars():
    with open("DisplayCars_Data.txt", "a") as text:
        car_type = input("Type: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        text.write("\n%s:%s:%s:%s" % (car_type, brand, color, year))
 
 
def modify_cars():
    display_cars()
    with open("DisplayCars_Data.txt", "r") as text:
        index_to_modify = int(input("Select record to modify: "))
        lines = text.readlines()
        if index_to_modify - 1 >= len(lines) or index_to_modify < 0:
            print("Invalid index")
            return
        entries = []
        index = 0
        for line in lines:
            entries.append(line.rstrip().split(":"))
    with open("DisplayCars_Data.txt", "w") as text:
        car_type = input("Type: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        entries[index_to_modify - 1] = (car_type, brand, color, year)
        for entry in entries:
            text.write("%s:%s:%s:%s\n" % (entry[0], entry[1], entry[2], entry[3]))
 
 
def unregistered_function():
    while True:
        print("""
        ******** All Customers ********
        1. View all cars available for rent
        2. Register to SCRS 
        3. Exit to main menu
        """)
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number!")
            continue
 
        if choice == 1:
            display_cars()
 
        elif choice == 2:
            get_new_users()
            break
 
        elif choice == 3:
            break
 
        else:
            print("Please enter a choice between 1-2 only!")
 
 
def registered_function():
    if existing_users() is True:
        while True:
            print("""
            ******** Registered Customer ********
            1. Personal Rental History
            2. Available Cars
            3. Booking Cars 
            4. Payment and Confirmation of Booking
            5. Exit to main menu
            """)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number!")
                continue
 
            if choice == 1:
                print("personal history")  # personal_rental_history function goes here
 
            elif choice == 2:
                display_cars()
 
            elif choice == 3:
                book_cars()
 
            elif choice == 4:
                print("payment and confirmation")  # payment function goes here
 
            elif choice == 5:
                break
 
            else:
                print("Please enter a choice between 1-5 only!")
    else:
        print("1. Please re-enter login details")
        print("2. Exit to main menu")
        choice = int(input("Enter choice: "))
        if choice == 1:
            existing_users()
        else:
            return
 
 
# this function does not work
def book_cars():
    book_list = []
    with open("DisplayCars_Data.txt", "r") as text:
        lines = text.readlines()
        print(lines)
        select = int(input("Select Car for booking: "))
 
        for record in lines:
            rec = record.split(":")
            if select in rec[0]:
                counter = 0
                print("1.Type: ", rec[1])
                print("2.Brand: ", rec[2])
                print("3.Color: ", rec[3])
                print("4.Year: ", rec[4])
 
        if select >= len(lines) or select < 0:
            print("Error")
        list = []
 
 
if __name__ == "__main__":
    main()

