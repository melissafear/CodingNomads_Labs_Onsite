# Redo the exercises from '03_pgadmin.txt' in the SQL labs using SQLAlchemy .

from pprint import pprint
import sqlalchemy

import sqlalchemy

engine = sqlalchemy.create_engine(f'postgres+psycopg2://melissa@localhost:5432/car_dealership')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

#------------------------------------------------------------------------
# - select all records from users
# SELECT * FROM users

# users = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.select([users])
#
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)


#------------------------------------------------------------------------
#  - select all records from cars where car make = "Toyota"
# SELECT * FROM cars WHERE make = 'Toyota'

# cars = sqlalchemy.Table('cars', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.select([cars]).where(cars.columns.make =='Toyota')
#
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)



#------------------------------------------------------------------------
#     - use a join to select the first name and car model of every user who has bought a car
#
# SELECT users.first_name, cars.model  FROM users
# INNER JOIN users_cars ON users_cars."userID" = users.id
# INNER JOIN cars ON users_cars."carID" = cars.id

cars = sqlalchemy.Table('cars', metadata, autoload=True, autoload_with=engine)
users = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)
users_cars = sqlalchemy.Table('users_cars', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([users.columns.first_name, cars.columns.model]).where(cars.id == users.id)

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)




#------------------------------------------------------------------------
# - use a join to select the first and last name of everyone who has bought a red car
#
# SELECT users.first_name,users.last_name, cars.color
#   FROM users
# INNER JOIN users_cars ON users_cars."userID" = users.id
# INNER JOIN cars ON users_cars."carID" = cars.id
# WHERE cars.color = 'red';





#------------------------------------------------------------------------
#     - use an insert statement to create a new record in each table
#
# INSERT INTO public."users"("id", first_name,last_name)
# VALUES
#
# ('3','Grace', 'Hopper')
#
#------------------------------------------------------------------------
#     - use sql to update a record in the "cars" table
#
# UPDATE cars
# SET color = 'purple'
# WHERE id = 4;
#
#------------------------------------------------------------------------
# - delete one record from the database
#
# DELETE FROM users WHERE first_name='Robert';




