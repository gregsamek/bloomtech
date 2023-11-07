import sqlite3

connection = sqlite3.connect('demo_data.sqlite3')

cursor = connection.cursor()

CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS demo(
s VARCHAR(1) NOT NULL,
x INT NOT NULL,
y INT NOT NULL
);
'''

cursor.execute(CREATE_TABLE)
connection.commit()

for row in [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]:
    cursor.execute(f"INSERT INTO demo (s, x, y) VALUES {row}")
connection.commit()

row_count = cursor.execute('SELECT COUNT(*) FROM demo').fetchall()

xy_at_least_5 = cursor.execute(
    """
    SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5
    """
    ).fetchall()

unique_y = cursor.execute('SELECT COUNT(DISTINCT y) FROM demo').fetchall()
