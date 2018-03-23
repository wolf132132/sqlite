import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "authorupdate@update.com"
phone = input("Inout the phone number")

update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
# update_sql = "UPDATE contacts SET email = 'authorupdate@update.com' WHERE phone = 1234"

update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("Are connections the same {}".format(update_cursor.connection == db))
print()
update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()