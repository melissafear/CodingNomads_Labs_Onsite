'''

All of the following exercises should be done using sqlalchemy.

Using the dvdrental schema, write the necessary code to print information about the film and category table.

'''



from pprint import pprint
import sqlalchemy

import sqlalchemy


engine = sqlalchemy.create_engine(f'postgres+psycopg2://melissa@localhost:5432/dvdrental')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)


print(film.columns.keys())
print(repr(metadata.tables['film']))

print(category.columns.keys())
print(repr(metadata.tables['category']))