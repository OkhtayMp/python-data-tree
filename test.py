# Import required modules
from datatree import print_tree  # For visualizing data structures
from datetime import date  # For handling dates

# Define a custom User class to demonstrate object visualization
class User:
    """Represents a user with name and age attributes"""
    def __init__(self, name: str, age: int):
        self.name = name  # User's name (string)
        self.age = age    # User's age (integer)

# Define a function to demonstrate callable visualization
def calculate_score(user: User) -> float:
    """Calculates a score based on user's age"""
    return user.age * 1.5  # Simple calculation for demonstration

# Create sample user objects
users = [
    User("Alice", 28),  # User instance 1
    User("Bob", 35),    # User instance 2
    User("Charlie", 42) # User instance 3
]

# Build a comprehensive test data structure demonstrating various Python types
test_data = {
    # Metadata section - basic information
    "metadata": {
        "created": date(2023, 5, 15),  # Date object
        "author": "Test Suite",        # String
        "version": 1.2                 # Float
    },
    
    # Users section - contains list of User objects
    "users": users,  # Reference to previously defined users list
    
    # Calculations section - demonstrates derived data
    "calculations": {
        "scores": [calculate_score(u) for u in users],  # List comprehension
        "average": sum(u.age for u in users) / len(users)  # Average calculation
    },
    
    # Data types section - comprehensive type coverage
    "data_types": {
        # Primitive types
        "primitives": {
            "integer": 42,     # int
            "float": 3.14,     # float
            "string": "hello", # str
            "boolean": True,   # bool
            "none": None       # NoneType
        },
        
        # Collection types
        "collections": {
            "list": [1, 2, 3],          # List
            "tuple": (4, 5, 6),         # Tuple
            "set": {7, 8, 9},           # Set
            "dict": {"a": 1, "b": 2}   # Dictionary
        },
        
        # Special Python types
        "special": {
            "binary": b'\x01\x02\x03',          # Bytes
            "function": calculate_score,        # Function
            "class": User,                      # Class reference
            "exception": ValueError("Sample error"),  # Exception
            "range": range(5)                   # Range
        }
    }
}

# Print demonstration header
print("Comprehensive Data Structure Demonstration:")

# Visualize the complete test data structure
print_tree(test_data)