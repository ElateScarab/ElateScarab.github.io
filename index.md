# **About Me: (this is where my professional assessment will go)**
Welcome to my ePortfolio! My name is Thor Nielssen, and I have been enrolled at SNHU since August 2021.
This ePortfolio serves as my final project for the course.

## **My video code review:**
[Link to Video Code Review hosted on ScreenPal](https://go.screenpal.com/watch/cZh0rqVLGiY)

In this video, I review the artifacts I selected for this course and break them down.
Please note that one of these artifacts, an API, did not make it into my final project.
I instead added another enhancement category to my IT145 artifact.

## **My original artifact for enhancement:**
[Original Artifact Folder](https://github.com/ElateScarab/ElateScarab.github.io/tree/c1516d5f3db2a85e73c74df677ff26e5422fff66/Original%20Artifact)

This artifact came from IT145 (Foundation in Application Development), where it was originally written in Java and centered around basic array lists used to manage a rescue animal system. My enhancements for each category were applied to this artifact, to the point that the final product is nearly unrecognizable from the original. I selected this artifact because it represents my earliest work, and my enhancements show just how much I have learned at SNHU and how far I have come.

# **My final product:**
[Final Artifact Folder](https://github.com/ElateScarab/ElateScarab.github.io/tree/c1516d5f3db2a85e73c74df677ff26e5422fff66/Final%20Artifact/Final%20Artifact)

## **Link to the original narratives:**
[Enhancement Narratives](https://github.com/ElateScarab/ElateScarab.github.io/tree/abde04be5f6c5c243b07e4cc88c2bbc22abfb4cf/Narratives)

## **Enhancement 1: Software Engineering and Design**
[Enhancement 1](https://github.com/ElateScarab/ElateScarab.github.io/tree/a30736548245e46ba6c803374df2e69add698b22/Enhancement%201)

### About this enhancement:
My first artifact for enhancement is the Animal Shelter project from IT145, which was written in Java. The program runs in a console window with a menu that allows a user to view and edit a list of rescue animals, which consists of dogs and monkeys. This project was created over two years ago in April 2022.
  
I included this artifact because it reflects some of my earliest work and left a lot of room for improvement, although the original project was completed satisfactorily to fulfill the IT145 project requirements. This artifact contains multiple classes to adhere to the principle of object-oriented programming, as well as multiple array lists and a long list of custom methods used to access, read from, and write to the array lists within the program. These classes and methods make this program more than just a simple console application because they show that I have a grasp on more advanced and industry best practice principles of programming.
  
I have improved this artifact by re-doing it from Java into Python, which not only made the program’s syntax much simpler but also reduced the amount of code required. The new program is cleaner, more concise, and generally a more professional product. This improvement also sets the stage for a later enhancement in the Databases category since Python is generally easier to use for database integration than Java, at least in my experience.
  
I feel that this enhancement effectively meets the outcomes I originally intended for it because it required quite a bit of research and redesign to properly translate it from one language to another, especially given that Java and Python do not share any common syntax, even in commenting the code. This meant that I had to manage the trade-offs between one language and the other, so a few major aspects of the program’s structure have changed accordingly. This enhancement also demonstrates the use of well-founded techniques, skills, and tools to accomplish industry-specific goals, because I had to start the Python program from scratch and design each class and method in accordance with everything I’ve learned in the past two years since the artifact was originally created. I feel that this properly displays my programming skills because even with an existing program to use as an outline, every single method and object in the code had to change for the new language.
  
I do not have any updates to my outcome coverage plans yet, although I would argue that this enhancement also created a more professional product that would be more valuable in a collaborative environment since it is so much cleaner and well-commented. The original Java project would not have stood up in a collaborative and team-based environment, but the new program in Python would be much easier for someone else to read and understand, then add to or edit the code.
    
The biggest thing that I learned during this creation and improvement process is that I am better at programming and code design than I thought I was. I spent the first four or five days of working on this project in the design stage alone, re-learning a lot of Python and trying to understand the Python alternatives to all the tools and syntax in the Java code. In this process, I learned that Python contains enough built-in functions and libraries that I did not need any of the libraries that were being imported into the Java program. I also learned that when translating from one language to another, there is no way to copy-paste or directly translate these programs, necessitating a full redesign and rebuild. 
    
One of the biggest challenges in this enhancement was ensuring that the menu logic worked – it took several iterations and a couple of sessions with SNHU tutoring services to completely grasp class inheritance in Python, for example, making the subclass options visible to the parent and driver class by using “super().” in front of the object attributes. Another challenge that took time to overcome was initializing everything with Python’s “init” statements in the class constructors as well as the main menu code. I feel that these challenges were overcome, and through a lot of design and trial and error, this enhancement fulfills at least the two original outcomes I had planned for it, if not also the collaboration-focused outcome for the reasons detailed in the previous section.
    
## **Enhancement 2: Data Structures and Algorithms**
[Final Project w/Algorithm Implementation](https://github.com/ElateScarab/ElateScarab.github.io/tree/abde04be5f6c5c243b07e4cc88c2bbc22abfb4cf/Final%20Artifact/Final%20Artifact)

### About this enhancement:
Once again, this is my Rescue Animal (Shelter) project from IT145. The original artifact was created in 2022 but has already been enhanced by the first and third enhancement categories. Re-done in from Java into Python and having a full database and relevant functions added to it, this project now includes algorithms used to search, sort, and manage the data and data structures in the program.

I selected this artifact for this enhancement because once the program was re-done in another language and contained a database and data operators, it was perfectly primed for more improvement in usability and utility. This artifact demonstrates not only an understanding of the SQL and im-memory data structures needed to operate a program like this, but also a comprehension of the algorithmic structure required to adjust, sort, and organize the data contained in this program’s database.
	I improved this artifact by implementing multiple algorithms that affect the structure and organization of the database as well as the utility of the menu options. 

1. A new, complex algorithm was implemented that determines the training stage of each animal listed in the database and updates them accordingly based on how long it has been since the animal’s original intake date.

2. Another function was added to the menu options to print a list of the animals in the database sorted by age.

3. A third algorithm was added that allows a user to delete entries from the database based on their ID; for example, a user could retrieve a list of animals and their IDs by selecting the menu option to print a list of all animals sorted by age, then use that list to find the ID of the animal they want to delete. I did not use the animal’s name for this function in case multiple animals have the same name.

I feel that this enhancement meets the intended course outcomes by demonstrating that I can use industry standard tools to create a useful application with relevant functions, and that I can use best practices and design tools to make sure that the program adequately and accurately fulfills its purpose.
I do not have any updates to my outcome coverage since this algorithm implementation was successful.

This enhancement was the hardest one yet, more so than translating from one language to another. My biggest challenge was learning and understanding how to implement the algorithm required to automatically update the animal’s training status based on intake time and date, as it required learning how to use the datetime libraries in Python and run calculations accordingly. However, I learned that moving a program’s data from in-memory arrays to a permanent database does not always solve an issue completely – understanding how a database operates and ensuring that you have the correct algorithms and functions implemented to use it is very important.

## **Enhancement 3: Databases**
[Database Enhancement](https://github.com/ElateScarab/ElateScarab.github.io/tree/abde04be5f6c5c243b07e4cc88c2bbc22abfb4cf/Enhancement%202)

### About this enhancement:
This artifact is my Rescue Animal final project from IT145. The project was originally done in early 2022, but it was also my first enhancement for this capstone course, when I redesigned and rebuilt it from its original Java code into Python. The Rescue Animal project used Java and array lists to store lists of monkeys and dogs to be reserved as service animals, allowing a user to input new animals as well as view the existing animal lists and reserve them based on input criteria.

I selected this item because it exemplifies some of my earliest programming work. The original Java program depended on array lists that were held in memory while the program ran, then purged when it ended. This program fulfilled the requirements for IT145 but now that I have taken many more programming classes, I learned many ways to improve it. The specific components of this artifact that needed improvement were the language in which it was written and the way it manipulated data. Java is a great object-oriented language, but since the original project depended on the aforementioned array lists, it would be immensely difficult to implement better data structures. Completely re-writing the application in Python made the code more concise and easier to read and demonstrated a thorough understanding of both languages and how to design code in each. It also better equipped me to further enhance the artifact in the databases category.

1.	I used SQLite, Python’s built-in SQL handler, to create a database with tables for each animal that lives in the same root folder as the rest of the application’s .py files.

2.	This SQLite database persists between each run of the application, meaning that all data stored in the database is stored permanently and is accessible each time the application runs, as opposed to the temporary array lists that were held in memory.

3.	The animal classes (Dog.py and Monkey.py) each contain more of their own dedicated code, reducing the complexity of the RescueAnimal.py and Driver.py classes.

4.	The menu now functions as a true menu loop, allowing a user to repeatedly select and engage with menu options until they either force stop the application or input “q” when selecting menu options.

I feel that this enhancement went a step beyond what I expected when I originally planned it and adequately meets the course outcomes I originally selected. The enhancement demonstrates effective software design choices in selecting a SQL technology to use, and properly addresses the databases requirement by creating a new database and all necessary methods and handlers to manipulate said database with SQL statements built into the Python code. I have no updates to my outcome coverage plans at this time since I feel that this enhancement came out better than I had hoped for.

When I started this project, I intended to use MySQL to implement the database requirements and I struggled for quite a while trying to make that work. It was only while troubleshooting why MySQL wasn’t working that I realized that Python’s native SQL handler, SQLite, was better suited for this sort of local database implementation. My biggest challenge was not creating the database, because SQLite’s documentation was clear on the basic statements required to create a database and the tables within it. Rather, the difficulty came in finding a way to get rid of the original array lists and related syntax and replace them with SQL operators and syntax to fulfill the same purpose, but better. This took long hours of research for such a short and concise program, but the end product demonstrates that I persevered and finally arrived at a well-designed and functional solution.
