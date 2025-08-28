from Task_1 import Person

'''
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int, gender: str, address: str, **kwargs):
        super().__init__(**kwargs)  

        try:
            age = int(age)  
            if not isinstance(name, str): 
                print("Plaease provide valid input types:- Name must be a string.")
                return
            
            if age < 0: 
                print("Plaease provide valid input types:- Age must be a non-negative integer.")
                return

            if not isinstance(gender, str): 
                print("Plaease provide valid input types:- Gender must be a string.")
                return

            if not isinstance(address, str):  
                print("Plaease provide valid input types:- Address must be a string.")
                return
            
        except Exception:
                print("Plaease provide valid input types:- Age must be an Integer")
                return

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

'''

class Employee(Person):
    counter = 0 # class variable to keep track of number of employees

    def __init__(self, salary: float, **kwargs):
        super().__init__(**kwargs)  # Call to super() for cooperative multiple inheritance

        try:
            salary = float(salary)  # Checking if salary is float
            if salary < 0:  # Checking if salary is non-negative
                print("Please provide a non-negative value for salary.")
                return

        except Exception:   # Catching any exception that occurs during type conversion
            print("Please provide a valid number for salary.")
            return

        Employee.counter += 1   # Incrementing employee counter
        self.__employee_id = f"EMP{Employee.counter:02d}"   # Generating employee ID
        self._salary = salary   # Protected attribute for salary

    @property
    def employee_id(self):  # Read-only property for employee ID
        return self.__employee_id
    
    @property   
    def counter(self):  # Property to access the class variable counter
        return Employee.counter

    @property
    def salary(self):   # Getter for salary to access the protected attribute
        return self._salary

    @salary.setter  
    def salary(self, value: float): # Setter for salary to modify the protected attribute
        if not isinstance(value, (int, float)): # Checking if value is number
            print("Please provide a valid number for salary.")
            return

        if value >= 0:  # Checking if value is non-negative
            self._salary = value    # if all ok then update salary
        else:
            print("Salary cannot be negative.")

    def increase_salary(self, amount: float):   # Method to increase salary
        try:
            amount = float(amount)  # Trying to convert amount to float
        except Exception:
            print("Please provide a valid number for salary.")
            return
        
        if not isinstance(amount, (int, float)):    # Checking if amount is number
            print("Please provide a valid number for salary.")
            return
        
        if amount > 0:  # Checking if amount is positive
            self._salary += amount  # if all ok then Increasing salary 
        else:
            print("Increase amount must be positive.")

    def decrease_salary(self, amount):  # Method to decrease salary
        try:
            amount = float(amount)  # Trying to convert amount to float
        except Exception:
            print("Please provide a valid number for salary.")
            return
        
        if not isinstance(amount, (int, float)):    # Checking if amount is number
            print("Please provide a valid number for salary.")
            return
        
        if amount > 0 and self._salary - amount >= 0:   # Checking if amount is positive and does not exceed current salary
            self._salary -= amount  # if all ok then Decreasing salary
        else:
            print("Decrease amount must be positive and not exceed salary.")

    def introduction(self): # Implementation of abstract method
        return (f"I am an employee with ID: {self.employee_id} and my salary is: {self.salary}.")


    def __del__(self):      # Destructor to decrement employee counter when an object is deleted
        Employee.counter -= 1


if __name__ == "__main__":
    
    emp1 = Employee(name="Sudip", age=21, gender="Male", address="Kolkata", salary=50000)
    print(emp1)
    print(f"Is {emp1.name} an adult? {emp1.is_adult(emp1.age)}")
    print(f"Number of employees: {emp1.counter}")
    print(emp1.greet(emp1))  # Employee greeting themselves
    print(emp1.introduction())
    print("-------" * 20)

    # Creating another Employee instance
    emp2 = Employee(name="Pritam", age=24, gender="Male", address="Delhi", salary=60000)
    print(emp2)
    print(f"Number of employees: {emp2.counter}")
    emp2.increase_salary(5000)
    print(f"New salary for {emp2.name}: {emp2.salary}")
    emp2.decrease_salary(200000)    # Trying to decrease more than current salary (error handling)
    emp2.decrease_salary('200a0')    # Trying to decrease with invalid type (error handling)
    print("-------" * 20)


    # Deleting an employee
    del emp1
    print(f"Number of employees after deleting one: {emp2.counter}")
