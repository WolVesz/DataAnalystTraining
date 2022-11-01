"""
Edit the query function to enble a user to edit a specified data table
Edit add person function to add a new record to the data table.
Edit the edit person function to enable edits to any record.

Do not edit any of the code already written.
"""

import os
import pandas as pd

from data.basic import people


def load_data():
    """
    Loads data.
    :return: data table
    """
    if 'people.csv' in os.listdir('./data'):
        return pd.read_csv(r'./data/people.csv').to_dict('records')
    else:
        from data.basic import people
        return people


def query(table, name: str = None, occupation: str = None, state: str = None, age: int = None):
    # I got confused here, was this suppose to find anyone in the dict, or just the oldest DA?
    found = []
    for i in table:
        qualifies = True
        if name is not None:
            if i['name'] != name:
                qualifies = False
        if occupation is not None:
            if i['occupation'] != occupation:
                qualifies = False
        if state is not None:
            if i['state'] != state:
                qualifies = False
        if age is not None:
            if i['age'] != age:
                qualifies = False
        if qualifies:
            found.append(i)

    """
    Allows a user to query a specified table for any information in the table.

    :param table:
    :param name:
    :param occupation:
    :param state:
    :param age:
    :return: records which meet the requested informatiion
    """
    return found


print(query(people, 'Tyler'))
print(query(people, None, 'Broker'))


def add_person(table, name, occupation: str = None, state: str = None, age: int = None):
    table.append({'name': name, 'occupation': occupation, 'state': state, 'age': age})

    """
    Adds a person to the data table

    :param table: Table to add a person to.
    :param name: Name of person to add to the table.
    :param occupation: Occupation to add to the person.
    :param state: State where the person lives.
    :param age: age o the person
    :return: table with the added person
    """
    return table


add_person(people, 'Matt Paquette', 'Medical Sales', 'California', 24)


def edit_person(table, name, occupation: str = None, state: str = None, age: int = None):
    for person in table:
        if person['name'] == name:
            if occupation is not None:
                person['occupation'] = occupation
            if state is not None:
                person['state'] = state
            if age is not None:
                person['age'] = age

    """
    edits a person to the data table

    :param table: Table to add a person to.
    :param name: Name of person to add to the table.
    :param occupation: Occupation to add to the person.
    :param state: State where the person lives.
    :param age: age o the person
    :return: table with the added person
    """
    return table


edit_person(people, 'Sean Holt', None, 'British Columbia', None)


def save_data(table):
    """
    Saves Data table to csv

    :param table: Table to be saved.
    :return: None
    """
    pd.DataFrame(table).to_csv(r'./data/people.csv', index=False)
