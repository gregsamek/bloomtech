import psycopg2
from os import getenv

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=getenv('DBNAME'), 
                        user=getenv('USER'),
                        password=getenv('PASSWORD'), 
                        host=getenv('HOST'))
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
print(cur.fetchall())