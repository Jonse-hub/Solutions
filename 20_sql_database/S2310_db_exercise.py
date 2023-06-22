"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Anvend det, du har lært i dette kapitel om databaser, på en første opgave.

Trin 1:
Opret en ny SQLite database "S2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""


# install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy.orm import declarative_base, Session
# the library sqlalchemy helps us to work with a database
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select

Database = 'sqlite:///20_sql_database/Customers_And_Product.db'
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Customer({self.name=}    {self.address=}    {self.age=})"

    """ def convert_to_tuple(self):  # Convert Person to tuple
        return self.id, self.name, self.age

    def valid(self):  # is this object a valid record of a person?
        try:
            value = int(self.age)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Person
        person = Person(id=tuple_[0], name=tuple_[1], age=tuple_[2])
        return person """


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Integer)
    brand = Column(String)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Product({self.product_number=}    {self.price=}    {self.brand=})"


def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


# return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
def get_record(classparam, record_id):
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(
            classparam.id == record_id)).first()
    return record


# Optional. Used to test data base functions before gui is ready.
def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Customer(name="peter", address="Taastrup 2", age=18))
        new_items.append(Customer(name="susan", address="Taastrup 4",  age=19))
        new_items.append(Customer(name="jane", address="Taastrup 6", age=21))
        new_items.append(Customer(name="harry", address="Taastrup 7",  age=20))

        # needs a fix:
        new_items.append(Product(product_number=1, price=44,  brand="Tesla"))
        new_items.append(Product(product_number=2, price=50,  brand="Maersk"))
        session.add_all(new_items)
        session.commit()


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

# create_test_data()

print(select_all(Customer))
print(get_record(Customer, 1))

print(select_all(Product))
print(get_record(Product, 1))

""" CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;  """
