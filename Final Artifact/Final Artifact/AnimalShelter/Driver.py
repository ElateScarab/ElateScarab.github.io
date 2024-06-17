# Import SQLite which was used for the database
import sqlite3

# DateTime libraries imported to allow the new algorithms to retrieve date/time data
from datetime import datetime, timedelta

# Importing the Dog and Monkey classes plus the new database functions that
# replaced the basic array list functions
from Dog import Dog, get_all_dogs, add_dog
from Monkey import Monkey, get_all_monkeys, add_monkey

# create tables for monkeys and dogs in the database if they don't already exist
# this function could be removed, but would need to be run again if the database 
# ever changes location or is deleted. Leaving it in place is harmless since it 
# will not actually run these SQL statements if the tables already exist.
def create_tables():
    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    # Create table for dogs
    c.execute('''
        CREATE TABLE IF NOT EXISTS dogs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT,
            gender TEXT,
            age TEXT,
            weight TEXT,
            acquisition_date TEXT,
            acquisition_country TEXT,
            training_status TEXT,
            reserved INTEGER,
            in_service_country TEXT
        )
    ''')

    # Create table for monkeys
    c.execute('''
        CREATE TABLE IF NOT EXISTS monkeys (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            gender TEXT,
            age TEXT,
            weight TEXT,
            tail_length TEXT,
            height TEXT,
            body_length TEXT,
            acquisition_date TEXT,
            acquisition_country TEXT,
            training_status TEXT,
            reserved INTEGER,
            in_service_country TEXT
        )
    ''')

    # Commit database changes
    conn.commit()
    conn.close()


create_tables()


def main():

    display_menu()


# This method prints the menu options
def display_menu():
    print("\n\n")
    print("\t\t\t\tRescue Animal System Menu")
    print("[1] Intake a new dog")
    print("[2] Intake a new monkey")
    print("[3] Reserve an animal")
    print("[4] Print a list of all dogs")
    print("[5] Print a list of all monkeys")
    print("[6] Print a list of all animals that are not reserved")
    print("[7] Search an animal by name from the database")
    print("[8] Print a list of animals in the database, sorted by age")
    print("[9] Update the training status of all animals based on their tenure")
    print("[0] Delete an animal from the database by their ID number")
    print("[q] Quit application")
    print()
    print("Enter a menu selection")

    user_input = input()
    if user_input == '1':
        intake_new_dog()
    elif user_input == '2':
        intake_new_monkey()
    elif user_input == '3':
        reserve_animal()
    elif user_input == '4':
        print_animals('4')
    elif user_input == '5':
        print_animals('5')
    elif user_input == '6':
        print_animals('6')
    elif user_input == '7':
        print("Enter the name of the animal to search:")
        name = input()
        search_animal_by_name(name)
    elif user_input == '8':
        sort_animals_by_age()
    elif user_input == '9':
        update_training_status()
    elif user_input == '0':
        delete_animal_by_id()
    elif user_input == 'q':
        exit(0)
    else:
        print("Select a valid menu option")  # Input validation for the menu
        display_menu()
        user_input = input()


# Method to add a new dog to the database
def intake_new_dog():
    print("What is the dog's name?")
    name = input()

    dogs = get_all_dogs()
    for dog in dogs:
        if dog[1].lower() == name.lower():
            print("\n\nThis dog is already in our system\n\n")
            return

    print("Breed:")
    breed = input()

    print("Gender:")
    gender = input()

    print("Age:")
    age = input()

    print("Weight:")
    weight = input()

    print("Date acquired:")
    acquisition_date = input()

    print("Country acquired:")
    acquisition_country = input()

    print("Training status:")
    training_status = input()

    print("Reserved? (true/false)")
    reserved = input().lower() == 'true'

    if reserved:
        print("Country of service:")
        in_service_country = input()
    else:
        in_service_country = ""

    dog = Dog(name, breed, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
    add_dog(dog)
    print("New dog has been added.")
    display_menu()


# Method to add a new monkey to the database
# This method is similar to the original array list editor, but 
# basic Python commands have been replaced with the proper SQL syntax
def intake_new_monkey():
    print("What is the monkey's name?")
    name = input()

    monkeys = get_all_monkeys()
    for monkey in monkeys:
        if monkey[1].lower() == name.lower():
            print("\n\nThis monkey is already in our system\n\n")
            return

    print("Species: ")
    species = input()
    if species.lower() not in ["capuchin", "guenon", "macaque", "marmoset", "squirrel monkey", "tamarin"]:
        print("We currently are not accepting this species of monkey.")
        return

    print("Gender: ")
    gender = input()

    print("Age: ")
    age = input()

    print("Weight: ")
    weight = input()

    print("Tail length: ")
    tail_length = input()

    print("Height: ")
    height = input()

    print("Body length: ")
    body_length = input()

    print("Acquisition date: ")
    acquisition_date = input()

    print("Acquisition country: ")
    acquisition_country = input()

    print("Training status: ")
    training_status = input()

    print("Reserved? (true/false)")
    reserved = input().lower() == 'true'

    if reserved:
        print("Country of service: ")
        in_service_country = input()
    else:
        in_service_country = ""

    monkey = Monkey(name, species, gender, age, weight, tail_length, height, body_length, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
    add_monkey(monkey)
    print("New monkey has been added.")
    display_menu()


# Method allowing a user to select an animal to reserve from the database
def reserve_animal():
    print("Enter desired animal type:")
    animal_type = input()
    print("Enter desired animal country:")
    in_service_country = input()

    if animal_type.lower() == "dog":
        dogs = get_all_dogs()
        for dog in dogs:
            if dog[10].lower() == in_service_country.lower():

                # Connects to the SQLite DB and sets the cursor so that the queried
                # animal can be found
                conn = sqlite3.connect('rescue_animals.db')
                c = conn.cursor()
                c.execute('UPDATE dogs SET reserved = 1 WHERE id = ?', (dog[0],))
                conn.commit()
                conn.close()
                print(dog[1] + " has been reserved for you.")
                break
        else:
            print("It doesn't look like we have a dog available that matches your criteria.")
            display_menu()

    elif animal_type.lower() == "monkey":
        monkeys = get_all_monkeys()
        for monkey in monkeys:
            if monkey[13].lower() == in_service_country.lower():

                # Connects to the SQLite DB and sets the cursor so that the queried
                # animal can be found
                conn = sqlite3.connect('rescue_animals.db')
                c = conn.cursor()
                c.execute('UPDATE monkeys SET reserved = 1 WHERE id = ?', (monkey[0],))
                conn.commit()
                conn.close()
                print(monkey[1] + " has been reserved for you.")
                break
        else:
            print("It doesn't look like we have a monkey available that matches your criteria.")
            display_menu()
    else:
        print("That is not a valid choice. Grazioso Salvare only trains dogs and monkeys at this time.")
        display_menu()


# Prints a list of animals based on the selection a user makes from the main menu
def print_animals(choice):
    if choice == '4':
        dogs = get_all_dogs()
        for dog in dogs:
            print(f"Name: {dog[1]} Training status: {dog[8]} Reserved: {dog[9]}")
            print("Country: " + dog[10])
            
            # Hyphens used as an attractive separator between lines of results
            print("----------")
        display_menu()
    elif choice == '5':
        monkeys = get_all_monkeys()
        for monkey in monkeys:
            print(f"Name: {monkey[1]} Training status: {monkey[11]} Reserved: {monkey[12]}")
            print("Country: " + monkey[13])
            print("----------")
        display_menu()
    elif choice == '6':
        print("Animals that are not currently reserved:")
        dogs = get_all_dogs()
        for dog in dogs:
            if not dog[9]:
                print(f"Name: {dog[1]} Type: Dog")
                print(f"Training status: {dog[8]} Country: {dog[10]}")
                print("----------")
        monkeys = get_all_monkeys()
        for monkey in monkeys:
            if not monkey[12]:
                print(f"Name: {monkey[1]} Type: Monkey")
                print(f"Training status: {monkey[11]} Country: {monkey[13]}")
                print("----------")
        display_menu()

# Search algorithm that will allow a user to search for a specific animal by name.
# Note that names are case-sensitive.
def search_animal_by_name(name):
    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    c.execute("SELECT * FROM dogs WHERE name = ?", (name,))
    dogs = c.fetchall()

    c.execute("SELECT * FROM monkeys WHERE name = ?", (name,))
    monkeys = c.fetchall()

    conn.close()

    if not dogs and not monkeys:
        print(f"No animals found with the name: {name}")
        display_menu()
    else:
        for dog in dogs:
            print(f"Dog found: {dog}")
        for monkey in monkeys:
            print(f"Monkey found: {monkey}")
        display_menu()

# Simple sorting algorithm that will order animals by age. This could 
# be useful to a user or admin that is auditing the lifespan and 
# likelihood of "retirement" of animals in the future.
def sort_animals_by_age():
    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    c.execute("SELECT * FROM dogs ORDER BY age")
    dogs = c.fetchall()

    c.execute("SELECT * FROM monkeys ORDER BY age")
    monkeys = c.fetchall()

    conn.close()

    print("Dogs sorted by age:")
    for dog in dogs:
        print(dog)

    print("-------------------------")
    print("Monkeys sorted by age:")
    for monkey in monkeys:
        print(monkey)
    
    display_menu()

# More involved algorithm that iterates through the database and automatically assigns
# a training status value based on how long the animal has been in training or in
# the database of available animals. This is helpful because an admin can enter as many
# animals as they want at a time, then the program will automatically sort them based
# on how long they have been in the system and assign them training statuses accordingly.

def update_training_status():
    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    # Define the training duration for each phase
    training_phases = [
        ("intake", timedelta(days=1)),
        ("Phase I", timedelta(days=30)),
        ("Phase II", timedelta(days=60)),
        ("in service", timedelta(days=120))
    ]

    # Ensure phases are sorted by duration
    training_phases.sort(key=lambda x: x[1])

    # Internal definition for the status updates
    # Several print statements that I used for debugging have been commented out,
    # otherwise there would be hundreds of lines of console output every time this 
    # menu option is called/selected.
    def update_animal_training_status(animal_type, animals):
        for animal in animals:
            animal_id, acquisition_date_str, current_phase = animal
            # print(f"{animal_type.capitalize()} ID: {animal_id}, Acquisition Date: {acquisition_date_str}, Current Phase: {current_phase}")

            try:
                acquisition_date = datetime.strptime(acquisition_date_str, '%m-%d-%Y')
            except ValueError:
                # print(f"Invalid date format for {animal_type} with ID {animal_id}: {acquisition_date_str}")
                continue

            time_in_training = datetime.now() - acquisition_date
            # print(f"Time in Training for {animal_type.capitalize()} ID {animal_id}: {time_in_training.days} days")

            new_phase = current_phase

            for phase, duration in training_phases:
                if time_in_training >= duration:
                    new_phase = phase
                    # print(f"{animal_type.capitalize()} ID {animal_id} eligible for phase: {phase}")

            if new_phase != current_phase:
                # print(f"Updating {animal_type.capitalize()} ID {animal_id} from {current_phase} to {new_phase}")
                c.execute(f"UPDATE {animal_type}s SET training_status = ? WHERE id = ?", (new_phase, animal_id))

    # Update training status for dogs
    c.execute("SELECT id, acquisition_date, training_status FROM dogs")
    dogs = c.fetchall()
    update_animal_training_status('dog', dogs)

    # Update training status for monkeys
    c.execute("SELECT id, acquisition_date, training_status FROM monkeys")
    monkeys = c.fetchall()
    update_animal_training_status('monkey', monkeys)

    conn.commit()
    conn.close()

    print("Training statuses have been updated.")
    display_menu()

# A basic algorithm that allows a user or admin to search an animal 
# and delete them by their unique ID number.
def delete_animal_by_id():
    print("Enter the type of animal to delete (dog/monkey):")
    animal_type = input().lower()
    print("Enter the id of the animal to delete:")
    animal_id = input()

    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    if animal_type == 'dog':
        c.execute("DELETE FROM dogs WHERE id = ?", (animal_id,))
    elif animal_type == 'monkey':
        c.execute("DELETE FROM monkeys WHERE id = ?", (animal_id,))
    else:
        print("Invalid animal type.")
        conn.close()
        return

    conn.commit()
    conn.close()
    print(f"{animal_type.capitalize()} with id {animal_id} has been deleted.")
    display_menu()

# Run the program
if __name__ == "__main__":
    main()
    display_menu()