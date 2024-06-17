# SQLite imported here too so that add_monkey and get_all_monkeys can be 
# properly object-oriented and compartmentalized within this subclass
import sqlite3
from RescueAnimal import RescueAnimal


# subclass Monkey is a child of RescueAnimal
class Monkey(RescueAnimal):
    #  Instance variables
    species = str()
    tailLength = str()
    height = str()
    bodyLength = str()

    #  Constructor
    def __init__(self, name, species, gender, age, weight, tail_length, height, body_length, acquisition_date,
                 acquisition_country, training_status, reserved, in_service_country):
        super(Monkey, self).__init__()
        super().set_name(name)
        super().set_animal_type(species)
        super().set_gender(gender)
        super().set_age(age)
        super().set_weight(weight)
        super().set_tail_length(tail_length)
        super().set_height(height)
        super().set_body_length(body_length)
        super().set_acquisition_date(acquisition_date)
        super().set_acquisition_location(acquisition_country)
        super().set_training_status(training_status)
        super().set_reserved(reserved)
        super().set_in_service_country(in_service_country)

    # Species-specific accessors only for monkeys
    def get_tail_length(self):
        return self.tailLength

    def get_height(self):
        return self.height

    def get_body_length(self):
        return self.bodyLength

# New SQL connector and syntax to use instead of previous array lists
def add_monkey(monkey):
    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO monkeys (name, species, gender, age, weight, tail_length, height, body_length, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (monkey.get_name(), monkey.get_animal_type(), monkey.get_gender(), monkey.get_age(), monkey.get_weight(), monkey.get_tail_length(),
          monkey.get_height(), monkey.get_body_length(), monkey.get_acquisition_date(), monkey.get_acquisition_location(), monkey.get_training_status(), monkey.get_reserved(), monkey.get_in_service_country()))

    conn.commit()
    conn.close()


def get_all_monkeys():
    conn = sqlite3.connect('rescue_animals.db')
    c = conn.cursor()

    c.execute('SELECT * FROM monkeys')
    monkeys = c.fetchall()

    conn.close()
    return monkeys