import sqlite3

conn = sqlite3.connect("contacts.sqlite")
name = input("please enter a name to search for ")

#use LIKE clause could avoid case sensitivity
# for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
for row in conn.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
    print(row)

conn.close()