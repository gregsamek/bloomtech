import sqlite3
import pandas as pd



connection = sqlite3.connect('../buddymove_holidayiq.sqlite3')

df = pd.read_csv('../buddymove_holidayiq.csv')

df.to_sql(name='buddymove', con=connection, if_exists='replace')

if __name__ == '__main__':
    cursor = connection.cursor()

    queries = [
        'SELECT COUNT(*) FROM buddymove;',
        'SELECT COUNT(*) FROM buddymove WHERE Nature >= 100 AND Shopping > 100;']

    for query in queries:
        result = cursor.execute(query).fetchall()
        print(result)