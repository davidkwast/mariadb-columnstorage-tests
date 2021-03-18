import subprocess
from itertools import product
from datetime import date

# from tqdm import tqdm


db_name = 'cs'
table_name = 'item_values'
rl = 26
rn = 1000

'''
DROP TABLE cs.item_values;

CREATE TABLE cs.item_values (
  `slug` varchar(16) NOT NULL,
  `date` date NOT NULL,
  `value` double NOT NULL
) ENGINE=Columnstore DEFAULT CHARSET=utf8;
'''

def send_data(data):
    
    process = subprocess.Popen(
        args = ['cpimport', db_name, table_name],
        stdin = subprocess.PIPE,
    )
    
    process.communicate(data)
    
    process.wait()


total = 0
records = []
count = 0
list_l1 = [chr(n) for n in range(65,65+rl)]
list_l2 = [chr(n) for n in range(65,65+rl)]
list_l3 = [chr(n) for n in range(65,65+rl)]
list_n1 = ['{:04d}'.format(n) for n in range(1,1+rn)]

# pbar = tqdm(total=rl*rl*rl*rn*20*12)
for slug_t in product(list_l1, list_l2, list_l3, list_n1):
    slug = ''.join(slug_t)
    # print(slug)
    
    for year in range(2021,2000, -1):
        for month in range(12,0,-1):
            # print(year, month)
            
            r_date = date(year, month, 1)
            
            value = year*1000 + month
            
            b_slug = slug.encode('ascii')
            b_date = r_date.isoformat().encode('ascii')
            b_value = '{}'.format(value).encode('ascii')
            
            bytes_list = [b_slug, b_date, b_value]
            
            payload = b'|'.join(bytes_list)
            
            records.append(payload)
            
            count += 1
    
    if count > 10_000_000:
        send_data( b'\n'.join(records) )

        print('-'*80)
        total += count
        print(total)
        print('='*80)

        # pbar.update(len(records))
        records = []
        count = 0

# process.

