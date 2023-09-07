import datetime

def main():
    # Display the welcome message
    print("Welcome to the Car Booking System!")

    # Get the user's choice
    print("1. Book a car")
    print("2. View my booking history")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    # Process the user's choice
    if choice == 1:
        # Book a car
        book_car()
    elif choice == 2:
        # View the user's booking history
        view_booking_history()
    elif choice == 3:
        # Exit the program
        print("Thank you for using the Car Booking System!")
        exit()
    else:
        # Invalid choice
        print("Invalid choice!")

def book_car():
    # Get the car information from the user
    car_type = input("Enter the car type: ")
    brand = input("Enter the brand: ")
    year = input("Enter the year: ")

    # Check if the car is available
    if is_car_available(car_type, brand, year):
        # Book the car
        book_car_details(car_type, brand, year)
        print("Car booked successfully!")
    else:
        # Car is not available
        print("Car is not available!")

def view_booking_history():
    # Get the user's name
    name = input("Enter your name: ")

    # Get the user's booking history
    booking_history = get_booking_history(name)

    # Print the booking history
    if booking_history:
        for booking in booking_history:
            print(booking)
    else:
        print("No booking history found!")

def is_car_available(car_type, brand, year):
    # TODO: Implement this function to check if the car is available
    return True

def book_car_details(car_type, brand, year):
    # TODO: Implement this function to book the car
    pass

def get_booking_history(name):
    # TODO: Implement this function to get the user's booking history
    return []

if __name__ == "__main__":
    main()
