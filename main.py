# Load the sqlite module and create a cursor to the database
import sqlite3
conn = sqlite3.connect('deck/collection.sqlite')
c = conn.cursor()

# Query columns of interest and print each row
# You can query all columns using `*` in place of field names
for row in c.execute('SELECT id, guid, flds, sfld FROM notes ORDER BY sfld'):
        # Each `row` will be a tuple with as many entries as field queried
        print(row)
        id = row[0]
        guid = row[1]
        flds = row[2]
        sfld = row[3]
        # (You cannot manipulate the database directly here)
