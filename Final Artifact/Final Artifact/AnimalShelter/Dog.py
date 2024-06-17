# SQLite imported here too so that add_dog and get_all_dogs can be 
# properly object-oriented and compartmentalized within this subclass
import sqlite3
from RescueAnimal import RescueAnimal


# subclass Dog is a child of RescueAnimal
class Dog(RescueAnimal):
    #  Instance variable
    breed = str()

    #  Constructor
    def __init__(self, name, breed, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved,
                 in_service_country):
        super(Dog, self).__init__()
        super().set_name(name)
        super().set_breed(breed)
        super().set_gender(gender)
        super().set_age(age)
        super().set_weight(weight)
        super().set_acquisition_date(acquisition_date)
        super().set_acquisition_location(acquisition_country)
        super().set_training_status(training_status)
        super().set_reserved(reserved)
        super().set_in_service_country(in_service_country)

    # Species-specific accessor only for dogs
    def get_breed(self):
        return self.breed

# New SQL connector and syntax to use instead of previous array lists
def add_dog(dog):
    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO dogs (name, breed, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (dog.get_name(), dog.get_breed(), dog.get_gender(), dog.get_age(), dog.get_weight(), dog.get_acquisition_date(),
          dog.get_acquisition_location(), dog.get_training_status(), dog.get_reserved(), dog.get_in_service_country()))

    conn.commit()
    conn.close()


def get_all_dogs():
    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    c.execute('SELECT * FROM dogs')
    dogs = c.fetchall()

    conn.close()
    return dogs