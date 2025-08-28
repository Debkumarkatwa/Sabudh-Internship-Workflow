from Task_2 import Employee

'''
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int, gender: str, address: str, **kwargs):
        super().__init__(**kwargs)  

        try:
            age = int(age)  
            if not isinstance(name, str): 
                print("Plaease provide valid input types:- Name must be a string.")
                exit(1)
            
            if age < 0: 
                print("Plaease provide valid input types:- Age must be a non-negative integer.")
                exit(1)

            if not isinstance(gender, str): 
                print("Plaease provide valid input types:- Gender must be a string.")
                exit(1)

            if not isinstance(address, str):  
                print("Plaease provide valid input types:- Address must be a string.")
                exit(1)
            
        except Exception:
                print("Plaease provide valid input types:- Age must be an Integer")
                exit(1)

        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

    def greet(self, other_person: 'Person') -> None: 
        if isinstance(other_person, Person):
            print(f"Hello {other_person.name}! My name is {self.name}.")
        else:
            print("Sorry! Can only greet another Person.")

    @staticmethod
    def is_adult(age: int) -> bool: 
        if not isinstance(age, int):
            print("Please provide a valid integer for age.")
            return False
        
        return age > 18

    @abstractmethod
    def introduction(self):    
        pass


class Employee(Person):
    counter = 0

    def __init__(self, salary: float, **kwargs):
        super().__init__(**kwargs)
        try:
            salary = float(salary)
            if salary < 0:
                print("Please provide a non-negative value for salary.")
                exit(1)

        except Exception:
            print("Please provide a valid number for salary.")
            exit(1)
        
        Employee.counter += 1
        self.__employee_id = f"EMP{Employee.counter:02d}"
        self._salary = salary

    @property
    def employee_id(self):
        return self.__employee_id
    
    @property
    def counter(self):
        return Employee.counter

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if not isinstance(value, (int, float)):
            print("Please provide a valid number for salary.")
            return

        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative.")

    def increase_salary(self, amount: float):
        try:
            amount = float(amount) 
        except Exception:
            print("Please provide a valid number for salary.")
            return
        
        if not isinstance(amount, (int, float)):
            print("Please provide a valid number for salary.")
            return
        
        if amount > 0:
            self._salary += amount
        else:
            print("Increase amount must be positive.")

    def decrease_salary(self, amount):
        try:
            amount = float(amount) 
        except Exception:
            print("Please provide a valid number for salary.")
            return
        
        if not isinstance(amount, (int, float)):
            print("Please provide a valid number for salary.")
            return
        
        if amount > 0 and self._salary - amount >= 0:
            self._salary -= amount
        else:
            print("Decrease amount must be positive and not exceed salary.")

    def introduction(self):
        print(f"I am an employee with ID: {self.employee_id} and my salary is: {self.salary}.")


    def __del__(self):
        Employee.counter -= 1
'''

class Teacher(Employee):
    counter = 0     # Counter for teacher IDs

    def __init__(self, subjects, **kwargs):
        super().__init__(**kwargs)  # Initialize parent classes
        Teacher.counter += 1    # Increment teacher counter
        self.__teacher_id = f"TEC{Teacher.counter:02d}" # Generate teacher ID

        # Ensuring subjects is a list (if a string is provided, split by commas)
        self.subjects = subjects if isinstance(subjects, list) else subjects.split(",")

    @property
    def counter(self):  # Property to access the class variable counter
        return Teacher.counter
    
    @property
    def teacher_id(self):   # Getter for teacher_id to access the private attribute
        return self.__teacher_id

    @property
    def employee_id(self):  # Overriding employee_id to prevent access from Teacher instances
        raise AttributeError(f"{self.__class__.__name__} object has no attribute employee_id.")

    def add_subject(self, subject:str): # Method to add a subject
        for sub in subject.split(","):  # Allow adding multiple subjects separated by commas
            sub = sub.strip().capitalize()  # Stripping any leading/trailing whitespace and capitalizing
            if sub not in self.subjects:    # Checking if subject already exists
                self.subjects.append(sub)
                
            print('current subjects list:', self.subjects)

    def remove_subject(self, subject:str):  # method to remove a subject
        for sub in subject.split(","):  # Allow removing multiple subjects separated by commas
            sub = sub.strip().capitalize()  # Stripping any leading/trailing whitespace and capitalizing
            if sub in self.subjects:    # Checking if subject exists
                self.subjects.remove(sub)
                
            else:
                print(f"{subject} not found in subjects list.")
            
            print('current subjects list:', self.subjects)

    def introduction(self): # Implementation of abstract method
        return (f"I am a teacher with ID: {self.teacher_id} and I teach the following subjects: {', '.join(self.subjects)}.")


    def __del__(self):  # Destructor to decrement teacher counter when an object is deleted
        Teacher.counter -= 1



if __name__ == "__main__":    # Creating Employee instances
    teacher1 = Teacher(name="swati", age=35, gender="Female", address="Mumbai", salary=75000, subjects=['Data Science', 'Machine Learning'])
    print(teacher1)
    print(teacher1.introduction())

    teacher1.add_subject("Python")
    teacher1.remove_subject("Machine Learning")

    teacher1.add_subject('Java, c, dsa, sql')  # Adding a new subject by string input
    print(teacher1.subjects)  # Displaying updated subjects list

    teacher1.remove_subject('c, dsa')  # Removing multiple subjects by string input
    print("------" * 20)

    teacher2 = Teacher(name="souvik", age=29, gender= 'male', address="Mumbai", salary=75000, subjects=['Data Science', 'Machine Learning', 'Python'])
    print(teacher2)
    print(teacher2.introduction())

    print(f"Number of teachers: {teacher2.counter}")
    teacher2.remove_subject("Java")  # Trying to remove a subject not in the list (error handling)
    teacher2.add_subject("Data Science")  # Trying to add a subject already in the list (error handling)

    print("------" * 20)

    # Test overridden employee_id attribute
    try:
        print(teacher1.employee_id)
    except AttributeError as e:
        print(f"Caught expected error: {e}")
    print("------" * 20)

    # deleting a teacher
    del teacher1
    print(f"Number of teachers after deleting one: {teacher2.counter}")
    print("------" * 20)

    # Test MRO
    print("Method Resolution Order (MRO) for Teacher class:")
    print((Teacher.mro()))
