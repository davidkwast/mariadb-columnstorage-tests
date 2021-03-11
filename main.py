


table_item_values = Table('item_values', metadata,
    Column('slug', String(16)),
    Column('date', String(32)),
    Column('value', String(32)),
    mysql_engine='Columnstore',
    mysql_charset='utf8',
)