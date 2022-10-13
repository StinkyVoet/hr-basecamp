'''
Create an application that manages contacts in an addressbook. The following requirements should be implemented:
- Add a contact with first name and last name (only alphabet), multiple (unique) e-mails (containing at least one '@'), 
  multiple (unique) phone numbers (only digits). Also, an ID should be generated which should be 1 higher than the highest current ID.
- Remove a contact by ID.
- List all contacts with the option to sort by first_name or last_name (default first_name) with a sort_by parameter 
  and in ascending (ASC) or decending (DESC) direction (default ASC) witb a direction parameter.
- Merge duplicate contacts (automatically). Contacts with the exact same full name (first and last name combined) should be merged. 
  The e-mails and phone numbers of the duplicate contacts should be added to the the first duplicate contact (contact with the highest ID). 
  The other duplicate contcts should be deleted from the addressbook.
- Contacts are read from the provided JSON file and should be updated with new or removed contacts.
'''

import os
import sys
import json

addressbook = []


def display(list = []):
    '''
    Print all contacts in the following format:

    ======================================
    
    Position: <position>
    First name: <firstname>
    Last name: <lastname>
    Emails: <email_1>, <email_2>
    Phone numbers: <number_1>, <number_2>
    '''

    print("======================================")
    print(f"Position: {list['id']}")
    print(f"First name: {list['first_name']}")
    print(f"Last name: {list['last_name']}")
    print(f"Emails: {', '.join(map(str,list['emails']))}")
    print(f"Phone numbers: {', '.join(map(str,list['phone_numbers']))}")


def list_contacts(sort_by: str, direction = 'ASC'):
    '''
    Return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
    '''

    reverse = False
    if direction.upper() == 'DESC':
        reverse = True

    sorted_list = sorted(addressbook, key=lambda d: d[sort_by], reverse=reverse)

    print(sorted_list)

    return addressbook


def add_contact(first_name: str, last_name: str, emails: set[str] = set(), phone_numbers: set[str] = set()):
    '''
    Add new contact:
    - first_name
    - last_name
    - emails = {}
    - phone_numbers = {}
    '''
    # todo: implement this function
    ...


def remove_contact(id: int):
    '''
    remove contact by ID (integer)
    '''
    # todo: implement this function
    ...


def merge_contacts():
    '''
    merge duplicates (automated > same fullname [firstname & lastname])
    '''
    # todo: implement this function
    ...


'''
read_from_json
Do NOT change this function
'''
def read_from_json(filename):
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in data:
            addressbook.append(contact)


'''
write_to_json
Do NOT change this function
'''
def write_to_json(filename):
    json_object = json.dumps(addressbook, indent = 4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)



def main(json_file):
    '''
    main function: build menu structure as following and call the appropriate functions:
    - the input can be case-insensitive (so E and e are valid inputs)
    - [E] Encode value to hashed value
    - [D] Decode hashed value to normal value
    - [P] Print all encoded/decoded values
    - [Q] Quit program
    Don't forget to put the contacts.json file in the same location as this file!
    '''

    read_from_json(json_file)

    # print(addressbook)
    # display([1, "voornaam", "achternaam", ["email1", "email2"], ["nummer1", "nummer2"]])

    # for contact in addressbook:
    #     display(contact)
    #     print(contact)

    # list_contacts('first_name', 'desc')

    match input('[L] List contacts\n[A] Add contact\n[R] Remove contact\n[M] Merge contacts\n[Q] Quit program').upper():
        case 'L':
            sort_by = input('Sort by: ')
            direction = input('Direction: ')
            list_contacts(sort_by, direction)
        case 'A':
            first_name = input('First Name: ')
            last_name = input('Last Name: ')
            emails = []
            
            add_contact(first_name, last_name, emails, phone_numbers)
    

'''
calling main function: 
Do NOT change it.
'''
if __name__ == "__main__":
    main('contacts.json')
