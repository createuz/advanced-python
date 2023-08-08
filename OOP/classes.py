# Class: Objects and Classes
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f'{self.make} {self.model}'


# Method: Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f'Balance: {self.__balance}'


# Method: Polymorphism
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def info(self):
        return f"Name: {self.name}\nAge: {self.age}\nMajor: {self.major}"

    def __str__(self):
        return self.info()


# Method: Inheritance
class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def describe(self):
        return f"Country: {self.name}\nPopulation: {self.population}\nCapital: {self.capital}"

    def __str__(self):
        return self.describe()


print('\nCar (Objects and Classes):')
car = Car("Toyota", "Corolla")
print(car)

print('\nBankAccount (Encapsulation):')
account = BankAccount("123456", 1000)
print(account)

print('\nStudent (Polymorphism):')
students = [
    Student("John", 20, "Computer Science"),
    Student("Emma", 22, "Engineering")
]
for student in students:
    print(student.info())

print('\nCountry (Inheritance):')
countries = [
    Country("Uzbekistan", 38261448, "Tashkent"),
    Country("United States", 331002651, "Washington"),
]

for country in countries:
    print(country.describe())
