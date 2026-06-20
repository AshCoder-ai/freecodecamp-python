"""
Medical Data Validator Module

This module provides functions to validate patient medical records against
specific data constraints (e.g., patient ID format, age limits, gender,
diagnosis, medications, and last visit ID format).
"""

import re

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    """
    Validates a single medical record's fields against specified constraints and returns the invalid fields.

    Constraints:
    - patient_id: Must be a string in the format 'p' followed by digits (case-insensitive).
    - age: Must be an integer greater than or equal to 18.
    - gender: Must be either 'male' or 'female' (case-insensitive).
    - diagnosis: Must be a string or None.
    - medications: Must be a list of strings.
    - last_visit_id: Must be a string in the format 'v' followed by digits (case-insensitive).

    Args:
        patient_id (any): The ID of the patient.
        age (any): The age of the patient.
        gender (any): The gender of the patient.
        diagnosis (any): The medical diagnosis.
        medications (any): The list of medications prescribed.
        last_visit_id (any): The ID of the patient's last visit.

    Returns:
        list of str: A list of keys/fields that failed validation.
    """
    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE), # r is for raw string, \d is for digit, + is for one or more
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }
    return [key for key, value in constraints.items() if not value]

def validate(data):
    """
    Validates a sequence of medical record dictionaries.

    Ensures the input is a list or tuple, each record is a dictionary, and
    each record contains all required keys. It then validates individual fields
    using `find_invalid_records` and prints format errors if any are found.

    Args:
        data (list or tuple): A collection of medical record dictionaries.

    Returns:
        bool: True if all records are formatted correctly and valid, False otherwise.
    """
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False

    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)

        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True

    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)