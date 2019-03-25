import sqlalchemy as db
import secrets
from slackclient import SlackClient
from pprint import pprint

slack_token = secrets.sl_secrets_tk
sc = SlackClient(slack_token)


engine = db.create_engine(f'postgres+psycopg2://melissa@localhost:5432/slack')
connection = engine.connect()
metadata = db.MetaData()

# film = db.Table('film', metadata, autoload=True, autoload_with=engine)
# category = db.Table('category', metadata, autoload=True, autoload_with=engine)



messages = db.Table('messages', metadata,
                    db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
                    db.Column('link', db.String(500), nullable = False),
                    db.Column('description', db.Text()),
                    db.Column('date_added', db.String(200)),
                    db.Column('read', db.Boolean, default=False),
                    db.Column('rating', db.Integer(), default=0),
                    db.Column('starred', db.Boolean(), default=False)
                    )


comments = db.Table('comments', metadata,
                    db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
                    db.Column('message_id', db.Integer(), db.ForeignKey('messages.id')),
                    db.Column('comment', db.String(500), nullable = True),
                    db.Column('author', db.String(100), nullable=False)

                    )

metadata.create_all(engine)