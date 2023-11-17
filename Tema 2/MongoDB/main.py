#pip install pymongo
from model.person import Person 
from model.newPerson import NewPerson
from data.mongo_operations import MongoDBOperations

mongo_operations = MongoDBOperations('person', 'people','27017')

personJohn = NewPerson(name='John Doe', age=30, email='john@example.com')
personJane = NewPerson(name='Jane Doe', age=25, email='jane@example.com')


mongo_operations.create_person(personJohn)
mongo_operations.create_person(personJane)

all_persons = mongo_operations.read_person({})
print("All persons:", all_persons)

# Update a person in the MongoDB collection
update_criteria = {'name': 'John Doe'}
update_data = {'age': 31}
updated_count = mongo_operations.update_person(update_criteria, update_data)
print(f"Updated {updated_count} person(s).")

# Read updated persons from the MongoDB collection
updated_persons = mongo_operations.read_person({})
print("Updated persons:", updated_persons)

# Delete a person from the MongoDB collection
delete_criteria = {'name': 'Jane Doe'}
deleted_count = mongo_operations.delete_person(delete_criteria)
print(f"Deleted {deleted_count} person(s).")

# Read remaining persons from the MongoDB collection
remaining_persons = mongo_operations.read_person({})
print("Remaining persons:", remaining_persons)