#pip install mysql-connector-python
import datetime
from data.db_operations import Database
from model.partido import Partido

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "my-secret-pw"
DB_DATABASE = "Futbol"
DB_PORT= "6969"


db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE,DB_PORT)


db.create_table()

partidoBase = Partido("Partidazo","Mestalla",1,3, datetime.date.today(), datetime.datetime(2023,6,14,7,12,39))


partidoDB=db.insert_data(partidoBase)


all_data = db.get_all_data()
print("All Data:")
for row in all_data:
    print(f'El partido con nombre {row[0]} tiene nombre {row[1]}')


partidoDataUpdated = (partidoDB[3],"Updated John Doe")
db.update_data(partidoDataUpdated)


updated_data = db.get_all_data()
print("\nUpdated Data:")
for row in updated_data:
    print(row)


db.delete_data(partidoDB[3])


after_deletion_data = db.get_all_data()
print("\nData After Deletion:")
for row in after_deletion_data:
    print(row)

db.close_connection()

