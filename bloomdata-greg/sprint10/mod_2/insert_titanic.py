import psycopg2
from os import getenv
import pandas as pd
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=getenv('DBNAME'), 
                        user=getenv('DB_USER'),
                        password=getenv('PASSWORD'), 
                        host=getenv('HOST'))

cur = conn.cursor()

def excom(query, conn=conn, cur=cur):
    cur.execute(query)
    conn.commit()

CREATE_ENUMS = '''
    CREATE TYPE survived AS ENUM ('0', '1');
    CREATE TYPE pclass AS ENUM ('1', '2', '3');
    CREATE TYPE sex AS ENUM ('male', 'female');
'''

TABLE_CREATION_QUERY = '''
    CREATE TABLE IF NOT EXISTS titanic(
            id SERIAL PRIMARY KEY,
            survived survived NOT NULL,
            pclass pclass NOT NULL,
            name VARCHAR(200) NOT NULL,
            sex sex NOT NULL,
            age FLOAT NOT NULL,
            sib_spouse INT NOT NULL,
            parents_children INT NOT NULL,
            fare FLOAT NOT NULL
    );
'''

if __name__ == '__main__':
    
    excom(CREATE_ENUMS)
    excom(TABLE_CREATION_QUERY)

    df = pd.read_csv('../titanic.csv')
    df['Name'] = df['Name'].str.replace("'", "")

    for row in df.itertuples():
        q = f'''
            INSERT INTO titanic (survived, pclass, name, sex, age, sib_spouse, parents_children, fare)
            VALUES ('{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', {row[5]}, {row[6]}, {row[7]}, {row[8]});
            ''' 
        excom(q)
