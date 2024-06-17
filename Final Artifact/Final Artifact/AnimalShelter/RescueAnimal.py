# Parent class RescueAnimal

class RescueAnimal:
    # Instance variables
    name = str()
    animal_type = str()
    gender = str()
    age = str()
    weight = str()
    acquisition_date = str()
    acquisition_country = str()
    training_status = str()
    reserved = bool()
    in_service_country = str()

    # Setting default values for each attribute
    def __init__(self):
        self.tail_length = None
        self.height = None
        self.body_length = None
        self.breed = None
        self.name = None
        self.animal_type = None
        self.gender = None
        self.age = None
        self.weight = None
        self.acquisition_date = None
        self.acquisition_country = None
        self.training_status = None
        self.reserved = False
        self.in_service_country = None

    # Accessors and mutators: these are the method definitions used by the Driver
    # class to get and set attributes for each animal

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_animal_type(self):
        return self.animal_type

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_acquisition_date(self):
        return self.acquisition_date

    def set_acquisition_date(self, acquisition_date):
        self.acquisition_date = acquisition_date

    def get_acquisition_location(self):
        return self.acquisition_country

    def set_acquisition_location(self, acquisition_country):
        self.acquisition_country = acquisition_country

    def get_reserved(self):
        return self.reserved

    def set_reserved(self, reserved):
        self.reserved = reserved

    def get_in_service_country(self):
        return self.in_service_country

    def set_in_service_country(self, in_service_country):
        self.in_service_country = in_service_country

    def get_training_status(self):
        return self.training_status

    def set_training_status(self, training_status):
        self.training_status = training_status

    def set_breed(self, breed):
        self.breed = breed

    def set_tail_length(self, tail_length):
        self.tail_length = tail_length

    def set_height(self, height):
        self.height = height

    def set_body_length(self, body_length):
        self.body_length = body_length
