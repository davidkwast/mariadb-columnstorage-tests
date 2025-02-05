from itertools import product
from datetime import date

from tqdm import tqdm
from decouple import config

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper


table_name = 'item_values__big'
rl = 26
rn = 100


engine = create_engine(config('DB_CONN'))


metadata = MetaData()

table_item_values = Table(
    table_name,
    metadata,
        Column('slug', String(16), nullable=False),
        Column('date', Date, nullable=False),
        Column('value', Float(53), nullable=False),
        # UniqueConstraint('slug', 'date', name='unique_slug_date'),
    mysql_engine='Columnstore',
    mysql_charset='utf8',
)


metadata.drop_all(engine, checkfirst=True)
metadata.create_all(engine, checkfirst=True)

metadata = MetaData()
table_item_values = Table(
    table_name,
    metadata,
        Column('slug', String(16), primary_key=True, nullable=False),
        Column('date', Date, primary_key=True, nullable=False),
        Column('value', Float(53), nullable=False),
        # UniqueConstraint('slug', 'date', name='unique_slug_date'),
    mysql_engine='Columnstore',
    mysql_charset='utf8',
)
class Table_Item_Values(object):
    def __init__(self, slug, date, value):
        self.slug = slug
        self.date = date
        self.value = value

mapper(Table_Item_Values, table_item_values)


Session = sessionmaker(bind=engine)
session = Session()

records = []
count = 0
list_l1 = [chr(n) for n in range(65,65+rl)]
list_l2 = [chr(n) for n in range(65,65+rl)]
list_l3 = [chr(n) for n in range(65,65+rl)]
list_n1 = ['{:04d}'.format(n) for n in range(1,1+rn)]

pbar = tqdm(total=rl*rl*rl*rn*20*12)
for slug_t in product(list_l1, list_l2, list_l3, list_n1):
    slug = ''.join(slug_t)
    # print(slug)
    
    for year in range(2021,2000, -1):
        for month in range(12,0,-1):
            # print(year, month)
            
            r_date = date(year, month, 1)
            
            value = year*1000 + month
            
            records.append(
                Table_Item_Values(
                    slug = slug,
                    date = r_date,
                    value = value
                )
            )
            
            count += 1
    
    if count > 250000:
        session.bulk_save_objects(records)
        session.commit()
        pbar.update(len(records))
        records = []
        count = 0
        # print('.', end='', flush=True)

session.bulk_save_objects(records)
session.commit()