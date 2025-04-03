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


<pre>Comprehensive Data Structure Demonstration:
<font color="#00AAAA">├── </font><font color="#8A8A8A">0</font> <font color="#BCBCBC">metadata</font> <font color="#AA5500">(</font><font color="#8A8A8A">dict</font><font color="#AA5500">)</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">├── </font><font color="#8A8A8A">0.0</font> <font color="#BCBCBC">created</font> <font color="#AA5500">(</font><font color="#8A8A8A">date</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">2023-05-15</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">├── </font><font color="#8A8A8A">0.1</font> <font color="#BCBCBC">author</font> <font color="#AA5500">(</font><font color="#8A8A8A">str</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">Test Suite</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">╰── </font><font color="#8A8A8A">0.2</font> <font color="#BCBCBC">version</font> <font color="#AA5500">(</font><font color="#8A8A8A">float</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">1.2</font>
<font color="#00AAAA">├── </font><font color="#8A8A8A">1</font> <font color="#BCBCBC">users</font> <font color="#AA5500">(</font><font color="#8A8A8A">list</font><font color="#AA5500">)</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">├── </font><font color="#8A8A8A">1.0</font> <font color="#AA5500">(</font><font color="#8A8A8A">User</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">&lt;__main__.User object at 0x75870d397ca0&gt;</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">├── </font><font color="#8A8A8A">1.1</font> <font color="#AA5500">(</font><font color="#8A8A8A">User</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">&lt;__main__.User object at 0x75870d397c40&gt;</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">╰── </font><font color="#8A8A8A">1.2</font> <font color="#AA5500">(</font><font color="#8A8A8A">User</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">&lt;__main__.User object at 0x75870d397be0&gt;</font>
<font color="#00AAAA">├── </font><font color="#8A8A8A">2</font> <font color="#BCBCBC">calculations</font> <font color="#AA5500">(</font><font color="#8A8A8A">dict</font><font color="#AA5500">)</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">├── </font><font color="#8A8A8A">2.0</font> <font color="#BCBCBC">scores</font> <font color="#AA5500">(</font><font color="#8A8A8A">list</font><font color="#AA5500">)</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">2.0.0</font> <font color="#AA5500">(</font><font color="#8A8A8A">float</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">42.0</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">2.0.1</font> <font color="#AA5500">(</font><font color="#8A8A8A">float</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">52.5</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">│   </font><font color="#00AA00">╰── </font><font color="#8A8A8A">2.0.2</font> <font color="#AA5500">(</font><font color="#8A8A8A">float</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">63.0</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">╰── </font><font color="#8A8A8A">2.1</font> <font color="#BCBCBC">average</font> <font color="#AA5500">(</font><font color="#8A8A8A">float</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">35.0</font>
<font color="#00AAAA">╰── </font><font color="#8A8A8A">3</font> <font color="#BCBCBC">data_types</font> <font color="#AA5500">(</font><font color="#8A8A8A">dict</font><font color="#AA5500">)</font>
    <font color="#AA00AA">├── </font><font color="#8A8A8A">3.0</font> <font color="#BCBCBC">primitives</font> <font color="#AA5500">(</font><font color="#8A8A8A">dict</font><font color="#AA5500">)</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">3.0.0</font> <font color="#BCBCBC">integer</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">42</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">3.0.1</font> <font color="#BCBCBC">float</font> <font color="#AA5500">(</font><font color="#8A8A8A">float</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">3.14</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">3.0.2</font> <font color="#BCBCBC">string</font> <font color="#AA5500">(</font><font color="#8A8A8A">str</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">hello</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">3.0.3</font> <font color="#BCBCBC">boolean</font> <font color="#AA5500">(</font><font color="#8A8A8A">bool</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">True</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">╰── </font><font color="#8A8A8A">3.0.4</font> <font color="#BCBCBC">none</font> <font color="#AA5500">(</font><font color="#8A8A8A">NoneType</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">None</font>
    <font color="#AA00AA">├── </font><font color="#8A8A8A">3.1</font> <font color="#BCBCBC">collections</font> <font color="#AA5500">(</font><font color="#8A8A8A">dict</font><font color="#AA5500">)</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">3.1.0</font> <font color="#BCBCBC">list</font> <font color="#AA5500">(</font><font color="#8A8A8A">list</font><font color="#AA5500">)</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">├── </font><font color="#8A8A8A">3.1.0.0</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">1</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">├── </font><font color="#8A8A8A">3.1.0.1</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">2</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">╰── </font><font color="#8A8A8A">3.1.0.2</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">3</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">3.1.1</font> <font color="#BCBCBC">tuple</font> <font color="#AA5500">(</font><font color="#8A8A8A">tuple</font><font color="#AA5500">)</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">├── </font><font color="#8A8A8A">3.1.1.0</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">4</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">├── </font><font color="#8A8A8A">3.1.1.1</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">5</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">╰── </font><font color="#8A8A8A">3.1.1.2</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">6</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">├── </font><font color="#8A8A8A">3.1.2</font> <font color="#BCBCBC">set</font> <font color="#AA5500">(</font><font color="#8A8A8A">set</font><font color="#AA5500">)</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">├── </font><font color="#8A8A8A">3.1.2.0</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">8</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">├── </font><font color="#8A8A8A">3.1.2.1</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">9</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">│   </font><font color="#0000AA">╰── </font><font color="#8A8A8A">3.1.2.2</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">7</font>
    <font color="#AA00AA">│   </font><font color="#00AA00">╰── </font><font color="#8A8A8A">3.1.3</font> <font color="#BCBCBC">dict</font> <font color="#AA5500">(</font><font color="#8A8A8A">dict</font><font color="#AA5500">)</font>
    <font color="#AA00AA">│   </font>    <font color="#0000AA">├── </font><font color="#8A8A8A">3.1.3.0</font> <font color="#BCBCBC">a</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">1</font>
    <font color="#AA00AA">│   </font>    <font color="#0000AA">╰── </font><font color="#8A8A8A">3.1.3.1</font> <font color="#BCBCBC">b</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">2</font>
    <font color="#AA00AA">╰── </font><font color="#8A8A8A">3.2</font> <font color="#BCBCBC">special</font> <font color="#AA5500">(</font><font color="#8A8A8A">dict</font><font color="#AA5500">)</font>
        <font color="#00AA00">├── </font><font color="#8A8A8A">3.2.0</font> <font color="#BCBCBC">binary</font> <font color="#AA5500">(</font><font color="#8A8A8A">bytes</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">b&apos;\x01\x02\x03&apos;</font>
        <font color="#00AA00">├── </font><font color="#8A8A8A">3.2.1</font> <font color="#BCBCBC">function</font> <font color="#AA5500">(</font><font color="#8A8A8A">function</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">&lt;function calculate_score at 0x75870d80fd90&gt;</font>
        <font color="#00AA00">├── </font><font color="#8A8A8A">3.2.2</font> <font color="#BCBCBC">class</font> <font color="#AA5500">(</font><font color="#8A8A8A">type</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">&lt;class &apos;__main__.User&apos;&gt;</font>
        <font color="#00AA00">├── </font><font color="#8A8A8A">3.2.3</font> <font color="#BCBCBC">exception</font> <font color="#AA5500">(</font><font color="#8A8A8A">ValueError</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">Sample error</font>
        <font color="#00AA00">╰── </font><font color="#8A8A8A">3.2.4</font> <font color="#BCBCBC">range</font> <font color="#AA5500">(</font><font color="#8A8A8A">range</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">range(0, 5)</font>

</pre>
