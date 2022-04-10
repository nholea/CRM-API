class Customer():
    def __init__(self, id, name, surname, email, birthdate):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.birthdate = birthdate

    def serialize(self):
        return{
            "id":self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "birthdate": self.birthdate
        }


customers= []

customer1 = Customer(1,"John", "Smith","jsmith@gmail.com","1992-09-15")
customer2 = Customer(2,"Sarah", "Wilson", "swil@outlook.com","1950-12-28")
customer3 = Customer(3,"Rachel","Davies","rachdvl@gmail.com","2000-01-16")

customers.append(customer1)
customers.append(customer2)
customers.append(customer3)
