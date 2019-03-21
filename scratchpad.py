test =  Table('testtable', metadata
              Column('id', Integer(), autoincrement=True, primary_keyTrue),
              Column('quote', String(255), nullable=False),
              Column('year', Integer()),

                     )
query = sqa.insert('testtable', metadata).values(
    quote = 'fdfdsffdsfdsfsd'
    year = 2007


)