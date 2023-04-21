from sqlalchemy import create_engine, MetaData, Integer, String,Text, Float, Table, Column

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()


measure = Table(
   'measure', meta,
   Column('station', String),
   Column('date', Text),
   Column('precip', Float),
   Column('tobs', Integer),
)
conn = engine.connect()
s = measure.select().where(measure.c.tobs > 70)
result = conn.execute(s)

for row in result:
   print(row)