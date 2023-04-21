from sqlalchemy_create_tables import measure, engine
import datetime 

ins = measure.insert()

# ins = measure.insert().values(station='USC00519397',	date='2010-01-01',	precip= 0.08, tobs=65)

# str(ins)
# 'INSERT INTO measure (station, date, precip, tobs) VALUES (station, date, precip, tobs)'


conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, [
    {'station':	'USC00519397',	'date':	'2010-01-01',	'precip':	0.08,	'tobs':	65},
    {'station':	'USC00519397',	'date':	'2010-01-02',	'precip':	0.0,	'tobs':	63},
    {'station':	'USC00519397',	'date':	'2010-01-03',	'precip':	0.0,	'tobs':	74},
    {'station':	'USC00519397',	'date':	'2010-01-04',	'precip':	0.0,	'tobs':	76},
    {'station':	'USC00519397',	'date':	'2010-01-06',	'precip':	0.0,	'tobs':	73},
    {'station':	'USC00519397',	'date':	'2010-01-07',	'precip':	0.06,	'tobs':	70},
    {'station':	'USC00519397',	'date':	'2010-01-08',	'precip':	0.0,	'tobs':	64},
    {'station':	'USC00519397',	'date':	'2010-01-09',	'precip':	0.0,	'tobs':	68},
    {'station':	'USC00519397',	'date':	'2010-01-10',	'precip':	0.0,	'tobs':	73},
    {'station':	'USC00519397',	'date':	'2010-01-11',	'precip':	0.01,	'tobs':	64}
])

