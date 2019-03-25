import sqlalchemy as db
import secrets
from slackclient import SlackClient
import json
from pprint import pprint

slack_token = secrets.sl_secrets_tk
sc = SlackClient(slack_token)


engine = db.create_engine(f'postgres+psycopg2://melissa@localhost:5432/slack')
connection = engine.connect()
metadata = db.MetaData()

messages = db.Table('messages', metadata, autoload=True, autoload_with=engine)

with open('mydata.json', 'r') as fin:
    mydata = json.load(fin)

pprint(mydata)

query = db.insert(messages)
connection.execute(query,mydata)


