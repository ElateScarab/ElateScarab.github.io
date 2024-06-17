import java.util.ArrayList;
import java.util.Scanner;

public class Driver {

    // Creating the array lists for Dog and Monkey
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();

    public static void main(String[] args) {

        initializeDogList();
        initializeMonkeyList();
        displayMenu();

        // Setting up the main menu options to reference the other methods

        Scanner scnr = new Scanner(System.in);
        char input = scnr.nextLine().charAt(0);
        switch (input) {
            case '1' -> intakeNewDog(scnr);
            case '2' -> intakeNewMonkey(scnr);
            case '3' -> reserveAnimal(scnr);
            case '4' -> printAnimals('4');
            case '5' -> printAnimals('5');
            case '6' -> printAnimals('6');
            case 'q' -> System.exit(0);
            default -> {
                System.out.println("Select a valid menu option"); // Input validation for the menu
                displayMenu();
            }
        }
    }

    // This method prints the menu options
    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter a menu selection");
    }


    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", true, "Canada");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
    }


    // Adds monkeys to a list for testing
    public static void initializeMonkeyList() {
        Monkey monkey1 = new Monkey("Jack", "Marmoset", "male", "3", "12", "14", "34", "40", "03-21-2018", "Peru", "in service", false, "United States");

        monkeyList.add(monkey1);
    }


    // Complete the intakeNewDog method
    // The input validation to check that the dog is not already in the list
    // is done for you
    public static void intakeNewDog(Scanner scnr) {

        System.out.println("What is the dog's name?");
        String name = scnr.nextLine();
        for (Dog dog : dogList) {
            if (dog.getName().equalsIgnoreCase(name))
            {
                System.out.println("\n\nThis dog is already in our system\n\n");
                return; //returns to menu
            }
            else {

                // Referencing the mutators in class RescueAnimal

                dog.setName(name);

                System.out.println("Breed:");
                dog.setBreed(scnr.nextLine());

                System.out.println("Gender:");
                dog.setGender(scnr.nextLine());

                System.out.println("Age:");
                dog.setAge(scnr.nextLine());

                System.out.println("Weight:");
                dog.setWeight(scnr.nextLine());

                System.out.println("Country acquired:");
                dog.setAcquisitionDate(scnr.nextLine());

                System.out.println("Date acquired:");
                dog.setAcquisitionLocation(scnr.nextLine());

                System.out.println("Training status:");
                dog.setTrainingStatus(scnr.nextLine());

                System.out.println("Reserved? (true/false)");
                dog.setReserved(scnr.nextBoolean());
                scnr.nextLine();

                if (dog.getReserved()) {
                    System.out.println("Country of service:");
                    dog.setInServiceCountry(scnr.nextLine());
                }
                System.out.println("New dog has been added.");

                displayMenu();
                return;
            }
        }
    }
    // Add the code to instantiate a new dog and add it to the appropriate list



        // Complete intakeNewMonkey
	//Instantiate and add the new monkey to the appropriate list
        // For the project submission you must also  validate the input
	// to make sure the monkey doesn't already exist and the species type is allowed
    public static void intakeNewMonkey(Scanner scnr) {

        System.out.println("What is the monkey's name?");
        String name = scnr.nextLine();
        for(Monkey monkey: monkeyList) {
            if(monkey.getName().equalsIgnoreCase(name)) {
            	System.out.println("\n\nThis monkey is already in our system\n\n");
            	return;
            }
            else
            {
                // Check the monkey species to make sure it is acceptable to Grazioso
                System.out.println("Species: ");
                monkey.setSpecies(scnr.nextLine());
                if(!(monkey.getSpecies().equalsIgnoreCase("Capuchin")) && !(monkey.getSpecies().equalsIgnoreCase("Guenon")) && !(monkey.getSpecies().equalsIgnoreCase("Macaque")) && !(monkey.getSpecies().equalsIgnoreCase("Marmoset")) && !(monkey.getSpecies().equalsIgnoreCase("Squirrel Monkey")) && !(monkey.getSpecies().equalsIgnoreCase("Tamarin")))
                {
                    System.out.println("We currently are not accepting this species of monkey.");
                    return;
                }

                // Reference mutators from class RescueAnimal to set attributes

                monkey.setName(name);

                System.out.println("Gender: ");
                monkey.setGender(scnr.nextLine());

                System.out.println("Age: ");
                monkey.setAge(scnr.nextLine());

                System.out.println("Weight: ");
                monkey.setWeight(scnr.nextLine());

                System.out.println("Tail length: ");
                monkey.setTailLength(scnr.nextLine());

                System.out.println("Height: ");
                monkey.setHeight(scnr.nextLine());

                System.out.println("Body length: ");
                monkey.setBodyLength(scnr.nextLine());

                System.out.println("Acquisition date: ");
                monkey.setAcquisitionDate(scnr.nextLine());

                System.out.println("Acquisition country: ");
                monkey.setAcquisitionLocation(scnr.nextLine());

                System.out.println("Training status: ");
                monkey.setTrainingStatus(scnr.nextLine());

                System.out.println("Reserved status: ");
                boolean reserved = scnr.nextBoolean();

                if (monkey.getReserved()) {
                    System.out.println("Country of service: ");
                    monkey.setInServiceCountry(scnr.nextLine());
                }
                System.out.println("New monkey has been added.");
                displayMenu();
                return;
            }
        }
    }

        // Complete reserveAnimal
        // You will need to find the animal by animal type and in service country
        public static void reserveAnimal(Scanner scnr) {
            System.out.println("Enter desired animal type: ");       // Querying user for animal type
            String type = scnr.nextLine();
            System.out.println("Enter desired animal country: ");    // Querying user for animal country
            String inServiceCountry = scnr.nextLine();
            if(type.equalsIgnoreCase("Dog"))
            {
                for (Dog dog : dogList) {
                    if (dog.getInServiceCountry().equals(inServiceCountry)) {
                        // Updating the reserved status
                        dog.setReserved(true);
                        System.out.println(dog.getName() + " has been reserved for you.");
                        break;
                    }
                }
                System.out.println("It doesn't look like we have a dog available that matches your criteria.");
                System.out.println("Please check your spelling or try another country.");
                displayMenu();
            }
            else if(type.equalsIgnoreCase("Monkey"))
            {
                for(Monkey monkey : monkeyList) {
                    if (monkey.getInServiceCountry().equals(inServiceCountry)) {
                        // Updating the reserved status
                        monkey.setReserved(true);
                        System.out.println(monkey.getName() + " has been reserved for you.");
                        break;
                    }
                    else {
                        System.out.println("It doesn't look like we have a monkey available that matches your criteria.");
                        System.out.println("Please check your spelling or try another country.");
                        displayMenu();
                    }
                }
            }
            else {
                System.out.println("That is not a valid choice. Grazioso Salvare only trains dogs and monkeys at this time.");
                System.out.println("Please check your spelling or enter a valid choice (dog or monkey).");
                displayMenu();
            }

        }

        // Complete printAnimals
        // Include the animal name, status, acquisition country and if the animal is reserved.
	// Remember that this method connects to three different menu items.
        // The printAnimals() method has three different outputs
        // based on the listType parameter
        // dog - prints the list of dogs
        // monkey - prints the list of monkeys
        // available - prints a combined list of all animals that are
        // fully trained ("in service") but not reserved 
	// Remember that you only have to fully implement ONE of these lists. 
	// The other lists can have a print statement saying "This option needs to be implemented".
	// To score "exemplary" you must correctly implement the "available" list.
        public static void printAnimals(char choice)
        {
            if(choice == '4')
            {                                         // Displays name, training status, reserved status, and country
                for (Dog dog : dogList) {
                    System.out.printf("%-5s %-10s %-7s %-10s %-9s %-10s %n", "Name:", dog.getName(), "Training status:", dog.getTrainingStatus(), "Reserved:", dog.getReserved());
                    System.out.println("Country: " + dog.getInServiceCountry());
                    System.out.println("----------");
                }
                displayMenu();
            }
            else if(choice == '5')
            {                                        // Displays name, training status, reserved status, and country
                for (Monkey monkey : monkeyList) {
                    System.out.printf("%-5s %-10s %-7s %-10s %-9s %-10s %n", "Name:", monkey.getName(), "Training status:", monkey.getTrainingStatus(), "Reserved:", monkey.getReserved());
                    System.out.println("Country: " + monkey.getInServiceCountry());
                    System.out.println("----------");
                }
                displayMenu();
            }
            else if(choice == '6')
            {
                System.out.println("Animals that are not currently reserved:");
                for (Dog dog : dogList) {
                    if(!dog.getInServiceCountry().isEmpty() && !dog.getReserved())
                    {
                        System.out.printf("%-5s %-10s %-5s %n", "Name:", dog.getName(), "Type: Dog");
                        System.out.println("Training status: " + dog.getTrainingStatus() + "   Country: " + dog.getInServiceCountry());
                        System.out.println("----------");
                    }
                }
                for (Monkey monkey : monkeyList)
                {
                    if(!monkey.getInServiceCountry().isEmpty() && !monkey.getReserved())
                    {
                        System.out.printf("%-5s %-10s %-5s %n", "Name:", monkey.getName(), "Type: Monkey");
                        System.out.println("Training status: " + monkey.getTrainingStatus() + "   Country: " + monkey.getInServiceCountry());
                        System.out.println("----------");
                    }
                }
                displayMenu();
            }
        }
}

