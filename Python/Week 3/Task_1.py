from abc import ABC, abstractmethod     # Importing Abstract Base Class and abstractmethod from abc module

class Person(ABC):
    def __init__(self, name: str, age: int, gender: str, address: str, **kwargs):   # assigning type hints to parameters
        super().__init__(**kwargs)  # Call to super() for cooperative multiple inheritance

        try:    # Checkung Input Values for better error handling
            age = int(age)  # Checking if age is integer
            if not isinstance(name, str):   # Checking if name is string
                print("Plaease provide valid input types:-\n Name must be a string.")
                return  # Exiting the constructor on invalid input
            
            if age < 0: # Checking if age is non-negative 
                print("Plaease provide valid input types:-\n\tAge must be a non-negative integer.")
                return

            if not isinstance(gender, str) or gender.capitalize() not in ['Male', 'Female', 'Others']: # Checking if gender is string and valid
                print("Plaease provide valid input types:-\n Gender must between [Male, Female, Others].")
                return

            if not isinstance(address, str):    # Checking if address is string
                print("Plaease provide valid input types:-\n Address must be a string.")
                return
            
        except Exception:   # Catching any exception that occurs during type conversion or validation(mainly for age conversion)
                print("Plaease provide valid input types:-\n Age must be an Integer")
                return

        self.name = name    # Assigning instance variables
        self.age = age      # Assigning instance variables
        self.gender = gender.capitalize()   # Assigning instance variables
        self.address = address  # Assigning instance variables

    def __str__(self):  # String representation of the object in print the object or str() function
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

    def greet(self, other_person: 'Person') -> None: # Type hinting with forward reference
        if isinstance(other_person, Person):    # Checking if the other_person is an instance of Person class
            return (f"Hello {other_person.name}! My name is {self.name}.")
        else:   # if not an instance of Person class for giving a poper message
            return ("Sorry! Can only greet another Person.")

    @staticmethod
    def is_adult(age: int) -> bool: # Static method to check if age is adult
        if not isinstance(age, int):    # Checking if age is integer (error handling)
            print("Please provide a valid integer for age.")
            return False
        
        return age > 18

    @abstractmethod
    def introduction(self):     # Abstract method to be implemented by subclasses
        pass

class Student(Person):      # test class inheriting Person class for showing functionality
    def introduction(self):
        print(f"{self.name} is studying.")


if __name__ == "__main__":  # safeguard as i need to import this file in task 2 & 3
    a = 'Test Object'


    # p1 = Person(name = 'Deb kumar Mondal', age = '21', gender= 'Male', address = 'Kolkata')

    # creating some wrong Student object to demonstrate error handling
    s1 = Student(name = 'Deb kumar Mondal', age = 21.6, gender= 'Male', address = 'Vill:- Panchghara, P.O- Khajurdihi, Dist- Purba Burddhaman, West Bengal, Pin- 713150')
    s2 = Student(name = 'Pritam Saha', age = 'abs', gender = 'Male', address = 'Kolkata')
    s1 = Student(name = 345, age = '21', gender= 'Male', address = 'Vill:- Panchghara, P.O- Khajurdihi, Dist- Purba Burddhaman, West Bengal, Pin- 713150')
    s2 = Student(name = 'Pritam Saha', age = 20, gender = 'unknown', address = 'Kolkata')
    s2 = Student(name = 'Pritam Saha', age = 20, gender = 'mAlE', address = 678)
    print('---'*30)

    # creating correct object
    s1 = Student(name = 'Deb kumar Mondal', age = '21', gender= 'male', address = 'Vill:- Panchghara, P.O- Khajurdihi, Dist- Purba Burddhaman, West Bengal, Pin- 713150')
    s2 = Student(name = 'Pritam Saha', age = 20, gender = 'Male', address = 'Kolkata')

    print('\nStudent-1 basic Information\n',s1)
    print('\nStudent-2 basic Information\n',s2)
    print('---'*30)

    print(s1.greet(s2))
    print(s1.greet(a))

    print('---'*30)
    print('Is the Person adult : ',Person.is_adult(20))
    print('Is the Person adult : ',Person.is_adult(17))
    print('Is the Person adult : ',s1.is_adult(s1.age))
    
    s1.introduction()  # This will work as Student implements introduction
    # p1.introduction()  # This will raise an error as Person is abstract and cannot be instantiated