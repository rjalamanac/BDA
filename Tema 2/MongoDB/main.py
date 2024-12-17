#pip install pymongo
#pip install Faker
from model.person import Person 
from model.newPerson import NewPerson
from data.mongo_operations import MongoDBOperations
from faker import Faker

fake = Faker()

mongo_operations = MongoDBOperations('federacion', 'arbitros','7777',username="mongoadmin",password="secret")

personJohn = NewPerson(name=fake.name(), age=fake.date_of_birth().__str__(), email=fake.email(),info=fake.word())
personJane = NewPerson(name=fake.name(), age=fake.date_of_birth().__str__(), email=fake.email(),info=fake.word())


mongo_operations.create_person(personJohn)
mongo_operations.create_person(personJane)

all_persons = mongo_operations.read_person({})
print("All persons:", all_persons)

# Update a person in the MongoDB collection
update_criteria = {'name': personJane.name}
update_data = {'age': 31}
updated_count = mongo_operations.update_person(update_criteria, update_data)
print(f"Updated {updated_count} person(s).")

# Read updated persons from the MongoDB collection
updated_persons = mongo_operations.read_person({})
print("Updated persons:", updated_persons)

# Delete a person from the MongoDB collection
delete_criteria = {'name': personJane.name}
deleted_count = mongo_operations.delete_person(delete_criteria)
print(f"Deleted {deleted_count} person(s).")

# Read remaining persons from the MongoDB collection
remaining_persons = mongo_operations.read_person({})
print("Remaining persons:", remaining_persons)

# Example aggregation pipeline
pipeline = [
    {"$group": {"_id": "$_id", "averageAge": {"$avg": "$age"}}},
    {"$sort": {"averageAge": -1}}
]

# Run the aggregation pipeline
result = mongo_operations.run_aggregation(pipeline)
print("Aggregation result:", result)