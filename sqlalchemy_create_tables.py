from sqlalchemy import Table, Column, Integer, String, MetaData,Date, Float,Text
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')


meta = MetaData()

measure = Table(
   'measure', meta,
   Column('station', String),
   Column('date', Text),
   Column('precip', Float),
   Column('tobs', Integer),
)

stations = Table(
   'stations', meta,
   Column('station', String,),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Float),
   Column('name', String),
   Column('country', String),
   Column('state', String),
)


meta.create_all(engine)
print(engine.table_names())