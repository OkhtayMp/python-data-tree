## Technical Demonstration

This example showcases the data structure visualizer's capabilities through:

1. **Comprehensive Type Support**:
   - Primitives (`int`, `float`, `str`, `bool`, `None`)
   - Collections (`list`, `tuple`, `set`, `dict`)
   - Special types (`bytes`, `function`, `class`, `exception`, `range`)
   - Custom objects (`User` class instances)

2. **Key Visualization Features**:
   - Hierarchical tree structure with proper indentation
   - Color-coded output (types, values, structure)
   - Type annotations in parentheses
   - Memory address display for objects
   - Special formatting for binary data and exceptions

3. **Nested Structure Handling**:
   - Multi-level dictionary nesting
   - Mixed collection types
   - Derived/computed values (scores, average)

The output clearly shows:
- Parent-child relationships via tree connectors
- Dot-notation indexing (e.g., 3.1.2.1)
- Consistent type-value formatting
- Proper handling of all Python built-in types
- Clean representation of custom objects

## Code

```python
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

```

## Output
This output is color-coded like the image: [Image](images/example.png)


```
Comprehensive Data Structure Demonstration:
├── 0 metadata (dict)
│   ├── 0.0 created (date) ▶ 2023-05-15
│   ├── 0.1 author (str) ▶ Test Suite
│   ╰── 0.2 version (float) ▶ 1.2
├── 1 users (list)
│   ├── 1.0 (User) ▶ <__main__.User object at 0x7f8665397ca0>
│   ├── 1.1 (User) ▶ <__main__.User object at 0x7f86653c4070>
│   ╰── 1.2 (User) ▶ <__main__.User object at 0x7f86653c7fd0>
├── 2 calculations (dict)
│   ├── 2.0 scores (list)
│   │   ├── 2.0.0 (float) ▶ 42.0
│   │   ├── 2.0.1 (float) ▶ 52.5
│   │   ╰── 2.0.2 (float) ▶ 63.0
│   ╰── 2.1 average (float) ▶ 35.0
╰── 3 data_types (dict)
    ├── 3.0 primitives (dict)
    │   ├── 3.0.0 integer (int) ▶ 42
    │   ├── 3.0.1 float (float) ▶ 3.14
    │   ├── 3.0.2 string (str) ▶ hello
    │   ├── 3.0.3 boolean (bool) ▶ True
    │   ╰── 3.0.4 none (NoneType) ▶ None
    ├── 3.1 collections (dict)
    │   ├── 3.1.0 list (list)
    │   │   ├── 3.1.0.0 (int) ▶ 1
    │   │   ├── 3.1.0.1 (int) ▶ 2
    │   │   ╰── 3.1.0.2 (int) ▶ 3
    │   ├── 3.1.1 tuple (tuple)
    │   │   ├── 3.1.1.0 (int) ▶ 4
    │   │   ├── 3.1.1.1 (int) ▶ 5
    │   │   ╰── 3.1.1.2 (int) ▶ 6
    │   ├── 3.1.2 set (set)
    │   │   ├── 3.1.2.0 (int) ▶ 8
    │   │   ├── 3.1.2.1 (int) ▶ 9
    │   │   ╰── 3.1.2.2 (int) ▶ 7
    │   ╰── 3.1.3 dict (dict)
    │       ├── 3.1.3.0 a (int) ▶ 1
    │       ╰── 3.1.3.1 b (int) ▶ 2
    ╰── 3.2 special (dict)
        ├── 3.2.0 binary (bytes) ▶ b'\x01\x02\x03'
        ├── 3.2.1 function (function) ▶ <function calculate_score at 0x7f866584bd90>
        ├── 3.2.2 class (type) ▶ <class '__main__.User'>
        ├── 3.2.3 exception (ValueError) ▶ Sample error
        ╰── 3.2.4 range (range) ▶ range(0, 5)
```