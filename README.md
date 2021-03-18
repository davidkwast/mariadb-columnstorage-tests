# mariadb-columnstorage-tests

```sql
set password for 'root'@localhost = password('xxxxx');

CREATE DATABASE cs;

CREATE TABLE cs.item_values(
  `slug` varchar(16) NOT NULL,
  `date` date NOT NULL,
  `value` double NOT NULL
) ENGINE=Columnstore DEFAULT CHARSET=utf8;
```

```
$ sudo python3 cpimport_stdin_test.py 
Locale = en_US.UTF-8
Using table OID 3000 as the default JOB ID
Input file(s) will be read from : STDIN
Job description file : /var/lib/columnstore/data/bulk/tmpjob/3000_D20210315_T230142_S731901_Job_3000.xml
Log file for this job: /var/lib/columnstore/data/bulk/log/Job_3000.log
2021-03-15 23:01:42 (7251) INFO : successfully loaded job file /var/lib/columnstore/data/bulk/tmpjob/3000_D20210315_T230142_S731901_Job_3000.xml
2021-03-15 23:01:42 (7251) INFO : Job file loaded, run time for this step : 0.0366461 seconds
2021-03-15 23:01:42 (7251) INFO : PreProcessing check starts
2021-03-15 23:01:42 (7251) INFO : PreProcessing check completed
2021-03-15 23:01:42 (7251) INFO : preProcess completed, run time for this step : 0.056638 seconds
2021-03-15 23:01:42 (7251) INFO : No of Read Threads Spawned = 1
2021-03-15 23:01:42 (7251) INFO : Reading input from STDIN to import into table cs.item_values__uber...
2021-03-15 23:01:42 (7251) INFO : No of Parse Threads Spawned = 3
2021-03-15 23:01:55 (7251) INFO : For table cs.item_values__uber: 50000076 rows processed and 50000076 rows inserted.
2021-03-15 23:01:56 (7251) INFO : Bulk load completed, total run time : 14.0964 seconds

--------------------------------------------------------------------------------
```