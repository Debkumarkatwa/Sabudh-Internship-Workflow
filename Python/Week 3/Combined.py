# full_solution.py

from abc import ABC, abstractmethod

# Task 1: Creating a Class (Abstraction)
class Person(ABC):
    def __init__(self, name, age, gender, address, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

    def greet(self, person_instance):
        print(f"Hello {person_instance.name}! My name is {self.name}.")

    @staticmethod
    def is_adult(age):
        return age >= 18

    @abstractmethod
    def introduction(self):
        print('Hello, I am a person.')

# Task 2: Single Inheritance, Encapsulation
class Employee(Person):
    counter = 0

    def __init__(self, salary, **kwargs):
        super().__init__(**kwargs)
        Employee.counter += 1
        self.__employee_id = f"EMP{Employee.counter:02d}"
        self._salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative.")

    def increase_salary(self, amount):
        if amount > 0:
            self._salary += amount
        else:
            print("Increase amount must be positive.")

    def decrease_salary(self, amount):
        if amount > 0 and self._salary - amount >= 0:
            self._salary -= amount
        else:
            print("Decrease amount must be positive and not exceed salary.")

    def introduction(self):
        print(f"I am an employee with ID: {self.employee_id} and my salary is: {self.salary}.")

    @property
    def num_employees(self):
        return Employee.counter

    def __del__(self):
        Employee.counter -= 1

# Task 3: Multiple Inheritance, Polymorphism
class Teacher(Employee):
    counter = 0

    def __init__(self, subjects, **kwargs):
        super().__init__(**kwargs)
        Teacher.counter += 1
        self.__teacher_id = f"TEC{Teacher.counter:02d}"
        self.subjects = subjects

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def employee_id(self):
        raise AttributeError(f"{self.__class__.__name__} object has no attribute employee_id.")

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"{subject} added.")

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
            print(f"{subject} removed.")
        else:
            print(f"{subject} not found in subjects list.")

    def introduction(self):
        print(f"I am a teacher with ID: {self.teacher_id} and I teach the following subjects: {', '.join(self.subjects)}.")

    @property
    def num_teachers(self):
        return Teacher.counter

    def __del__(self):
        Teacher.counter -= 1

# Example usage to demonstrate functionality
if __name__ == "__main__":
    # Create Person instance (note: this will raise an error if not handled properly as Person is abstract)
    # The assignment implies we will only create instances of the child classes.

    # Create Employee instance
    emp1 = Employee(name="Sudip", age=22, gender="Male", address="Kolkata", salary=50000)
    print(emp1)
    print(f"Is {emp1.name} an adult? {emp1.is_adult(emp1.age)}")
    print(f"Number of employees: {emp1.num_employees}")
    emp1.introduction()
    print("--------------------")

    # Create another Employee instance
    emp2 = Employee(name="Pritam", age=24, gender="Male", address="Delhi", salary=60000)
    print(emp2)
    print(f"Number of employees: {emp2.num_employees}")
    emp2.increase_salary(5000)
    print(f"New salary for {emp2.name}: {emp2.salary}")
    print("--------------------")

    # Create Teacher instance
    teacher1 = Teacher(name="Jane", age=35, gender="Female", address="Mumbai", salary=75000, subjects=['Data Science', 'Machine Learning'])
    print(teacher1)
    teacher1.introduction()
    teacher1.add_subject("Python")
    teacher1.remove_subject("Machine Learning")
    print("--------------------")

    # Test overridden employee_id attribute
    try:
        print(teacher1.employee_id)
    except AttributeError as e:
        print(f"Caught expected error: {e}")
    print("--------------------")

    # Test MRO
    print("Method Resolution Order (MRO) for Teacher class:")
    print(Teacher.mro())