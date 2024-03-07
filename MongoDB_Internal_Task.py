from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import re

uri = "mongodb+srv://rezan:rezan@cluster0.g4aqwe2.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    # print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

record = MongoClient("mongodb+srv://rezan:rezan@cluster0.g4aqwe2.mongodb.net/?retryWrites=true&w=majority").InternalTask.MongoDB


def Create_Contact():
    Name = str(input("Enter the name: "))
    try:
        print("The number must be in the range of 1-10.")
        Number = input("Enter the Mobile_Number:")
        if len(Number) == 10 and Number.isdigit():
            print("Mobile_Number Is Succesfully Created")
            
            Email = str(input("Enter the Email_ID: "))
            if Email.count('@') == 1:  
                if Email.count('.com') == 1:
                    print("Email Is Succesfully Created")
    except Exception as e:
        print(e)

    data = {"_id":Name,
            "Mobile_Number":Number,
            "Email_ID":Email}
    record.insert_one(data)

    return (data)
            
def Search_Contact():
    Search = input("Enter the name you Saved or 10 digit number you want to search for:")
    results = record.find({"$or": [{"_id": {"$regex": Search, "$options": "i"}},{"Mobile_Number": Search}]}).limit(20)
    for result in results:
        print(f"Name: {result['_id']}, Number: {result['Mobile_Number']}")
    return 

def Delete_Contact():
    search = input("Enter the name of the contact you want to delete: ")
    result = record.delete_one({"_id": search})
    if result.deleted_count == 1:
        print(f"Contact {search} deleted successfully.")
    else:
        print("Contact not found.")

def Display_all():
    contacts = record.find().limit(20)
    for contact in contacts:
        print(f"Name: {contact['_id']}, Number: {contact['Mobile_Number']}, Email_ID: {contact['Email_ID']}")
    return 

functions = [
    "1.Create_Contact",
    "2.Search_Contact",
    "3.Delete_Contact",
    "4.Display_all"
]
for i in functions:
    print(i)
user_input = input("Which one you want to do SELECT the number (1-4): ")

# Call the corresponding function based on user input
if user_input == '1':
    Create_Contact()
elif user_input == '2':
    Search_Contact()
elif user_input == '3':
    Delete_Contact()
elif user_input == '4':
  print(Display_all())
else:
    print("Invalid input. Please enter a number between 1 and 4.")