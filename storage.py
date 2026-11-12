import json
import os
from student import Student

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "students.json")

def save_data(students):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    data_list = [student.to_dict() for student in students]
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data_list, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, "r") as f:
            data_list = json.load(f)
            return [Student.from_dict(item) for item in data_list]
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading data file: {e}. Starting with an empty record list.")
        return []