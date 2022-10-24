"""
Edit the query function to enble a user to edit a specified data table
Edit add person function to add a new record to the data table.
Edit the edit person function to enable edits to any record.

Do not edit any of the code already written.
"""

import os
import pandas as pd


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
    """
    Allows a user to query a specified table for any information in the table.

    :param table:
    :param name:
    :param occupation:
    :param state:
    :param age:
    :return: records which meet the requested informatiion
    """
    return


def add_person(table, name, occupation: str = None, state: str = None, age: int = None):
    """
    Adds a person to the data table

    :param table: Table to add a person to.
    :param name: Name of person to add to the table.
    :param occupation: Occupation to add to the person.
    :param state: State where the person lives.
    :param age: age o the person
    :return: table with the added person
    """
    return


def edit_person(table, name, occupation: str = None, state: str = None, age: int = None):
    """
    edits a person to the data table

    :param table: Table to add a person to.
    :param name: Name of person to add to the table.
    :param occupation: Occupation to add to the person.
    :param state: State where the person lives.
    :param age: age o the person
    :return: table with the added person
    """
    return


def save_data(table):
    """
    Saves Data table to csv

    :param table: Table to be saved.
    :return: None
    """
    pd.DataFrame(table).to_csv(r'./data/people.csv', index = False)