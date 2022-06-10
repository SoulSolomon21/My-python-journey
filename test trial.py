
#number one Bus company


def login(username, password):
    # is_attendant = False
    user_password = "password"
    user_name = "Solomon"

    if username == user_name:
        if password == user_password:
            choice = str(input("Do you want to make a booking or a payment?"))
            if choice == 'yes':
                return True
            else:
                return False
            # is_attendant = True
    elif username != user_name and password != user_password:
        print("Wrong credentials, please enter the correct information")
        return False
    
def menu(choice):
    # if choice == 1:

    if choice == 2:
        available = 60
        seat_num = False
        print("--------Bus Booking--------")
        while seat_num == False:
            seats = int(input("Enter the number of seats you want to book: "))
            bus_type = int(input("Which type of bus do you want to board?\n For luxury bus, enter 1.\nFor ordinary bus, enter 2."))
            if seats > available:
                print(f"Please choose a number of seats that is equal to or less than {available}")
            elif seats <= available:
                if bus_type == 1 or bus_type == 2:
                    seat_num = True
                    menu_choice_2(seats,bus_type)
                else:
                    print("Please choose either 1 or 2")
    elif choice == 3:
        print("--------Booking payment--------")
        receipt = str(input("Enter your receipt number: "))
        amount = int(input("Enter the amount of money being paid: "))
        money = menu_choice_2(seats,bus_type)
        balance = money - amount
        

        
    # elif choice == 4:

    # elif choice == 5:

def menu_choice_2(seats,bustype):
    print(f"You have booked {seats} seats.")
    if bustype == 1:
        print("You have chosen a Luxury bus")
        total_cost = seats * 30000
        print(f"The total cost of the seats is {total_cost}")
    elif bustype == 2:
        print("You have chosen an ordinary bus type")
        total_cost = seats * 15000
        print(f"The total cost of the seats is {total_cost}")
    print(f"Your receipt number is B{bustype}S{seats}C{total_cost}")
    return total_cost

def Choices():
    menu_choice = False
    while menu_choice == False:
        print("-------------Menu--------------")
        print("1. Bus Booking Status")
        print("2. Bus Booking")
        print("3. Booking payment")
        print("4. Bus Booking reports")
        print("5. Sign out")
        choose = int(input("Choose an option from the menu above: "))

        if choose < 1 and choose > 5:
            print("Please choose an option from the menu")
        elif choose >=1 and choose <= 5:
            menu_choice = True
            return choose
        

def main():
    print("Soul bus")
    log = False
    while log == False:
        user = str(input("Please enter your name: "))
        pass_word = str(input("Please enter your password: "))
        log = login(user,pass_word)
        if log == True:
            choice = Choices()
            menu(choice)
            
main()
    
    











