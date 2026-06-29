

# ==========================================
# PARKING MANAGEMENT SYSTEM
# Mini Project in Python  
# ==========================================

# Import datetime module to store entry and exit time
from datetime import datetime

# Dictionary to store parked vehicle details
parking = {}

# Total parking slots available
TOTAL_SLOTS = 10

# Parking charge per hour
PARKING_FEE = 20



# ==========================================
# Main Menu Function
# ==========================================

def menu():
    print("\n====================================")
    print("     PARKING MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Parking Slot Availability")
    print("4. View Parked Vehicles")
    print("5. Exit")
    print("====================================")
    '''
    this code does
Creates the main menu.
Displays all options to the user.
We'll connect these options to functions in the next steps.'''

menu()

# ==========================================
# Function to Add Vehicle
# ==========================================

def vehicle_entry():

    # Check if parking is full
    if len(parking) >= TOTAL_SLOTS:
        print("\nSorry! Parking is Full.")
        return

    # Take vehicle details from the user
    vehicle_no = input("\nEnter Vehicle Number: ").upper()

    # Check if vehicle is already parked
    if vehicle_no in parking:
        print("This vehicle is already parked.")
        return

    vehicle_type = input("Enter Vehicle Type (Car/Bike/Bus): ")

    # Assign the next available parking slot
    slot = len(parking) + 1

    # Store current date and time
    entry_time = datetime.now()

    # Save vehicle details in dictionary
    parking[vehicle_no] = {
        "Type": vehicle_type,
        "Slot": slot,
        "Entry Time": entry_time
    }

    # Display success message
    print("\nVehicle Parked Successfully!")
    print("Parking Slot :", slot)
    print("Entry Time   :", entry_time.strftime("%d-%m-%Y %I:%M:%S %p"))


vehicle_entry()


# ==========================================
# Function to Check Parking Slot Availability
# ==========================================

def parking_status():

    # Calculate occupied and available slots
    occupied_slots = len(parking)
    available_slots = TOTAL_SLOTS - occupied_slots

    # Display parking status
    print("\n========== Parking Status ==========")
    print("Total Parking Slots     :", TOTAL_SLOTS)
    print("Occupied Parking Slots  :", occupied_slots)
    print("Available Parking Slots :", available_slots)

    # Check whether parking is full
    if available_slots == 0:
        print("\nParking is Full!")
    else:
        print("\nParking Slots are Available.")


parking_status()



# ==========================================
# Function for Vehicle Exit
# ==========================================

def vehicle_exit():

    # Check if parking is empty
    if len(parking) == 0:
        print("\nNo vehicles are parked.")
        return

    # Ask user for vehicle number
    vehicle_no = input("\nEnter Vehicle Number: ").upper()

    # Check whether vehicle exists
    if vehicle_no not in parking:
        print("Vehicle Not Found!")
        return

    # Get exit time
    exit_time = datetime.now()

    # Get entry time from dictionary
    entry_time = parking[vehicle_no]["Entry Time"]

    # Calculate parking duration in hours
    duration = (exit_time - entry_time).total_seconds() / 3600

    # If parked for less than 1 hour, charge for 1 hour
    if duration < 1:
        duration = 1

    # Calculate total fee
    total_fee = int(duration) * PARKING_FEE

    # Display bill
    print("\n========== Parking Bill ==========")
    print("Vehicle Number :", vehicle_no)
    print("Vehicle Type   :", parking[vehicle_no]["Type"])
    print("Parking Slot   :", parking[vehicle_no]["Slot"])
    print("Entry Time     :", entry_time.strftime("%d-%m-%Y %I:%M:%S %p"))
    print("Exit Time      :", exit_time.strftime("%d-%m-%Y %I:%M:%S %p"))
    print("Parking Hours  :", round(duration, 2))
    print("Total Fee      : ₹", total_fee)

    # Remove vehicle from parking
    del parking[vehicle_no]

    print("\nVehicle Exited Successfully!")

vehicle_exit()

# ==========================================
# Function to View All Parked Vehicles
# ==========================================

def view_parked_vehicles():

    # Check if parking is empty
    if len(parking) == 0:
        print("\nNo vehicles are currently parked.")
        return

    # Display heading
    print("\n========== Parked Vehicles ==========")

    # Display all parked vehicles
    for vehicle_no, details in parking.items():
        print("--------------------------------------")
        print("Vehicle Number :", vehicle_no)
        print("Vehicle Type   :", details["Type"])
        print("Parking Slot   :", details["Slot"])
        print("Entry Time     :", details["Entry Time"].strftime("%d-%m-%Y %I:%M:%S %p"))

    print("--------------------------------------")



# ==========================================
# Main Program
# ==========================================

while True:

    # Display menu
    menu()

    # Take user's choice
    choice = input("\nEnter your choice (1-5): ")

    # Call Vehicle Entry Function
    if choice == "1":
        vehicle_entry()

    # Call Vehicle Exit Function
    elif choice == "2":
        vehicle_exit()

    # Call Parking Status Function
    elif choice == "3":
        parking_status()

    # Call View Parked Vehicles Function
    elif choice == "4":
        view_parked_vehicles()

    # Exit the program
    elif choice == "5":
        print("\nThank You for Using Parking Management System!")
        print("Program Closed Successfully.")
        break

    # Invalid Choice
    else:
        print("\nInvalid Choice! Please Enter a Number Between 1 and 5.")    
