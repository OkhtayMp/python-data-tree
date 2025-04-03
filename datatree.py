from typing import Any, List, Optional
import inspect

def print_tree(data: Any) -> None:
    """
    Visualize nested Python data structures with ANSI-colored formatting.
    
    Features:
    - Color-coded hierarchy with different connector styles
    - Type information in parentheses
    - Index numbering for easy navigation
    - Support for dict, list, set, tuple and primitive types
    
    Color Scheme:
    - Indices & type text: Dark grey (low visibility)
    - Parentheses: Yellow
    - Dictionary keys: Light grey
    - Values: Light blue
    - Arrow: White
    - Connectors: Rotating colors per depth level
    
    Args:
        data: The Python data structure to visualize (dict/list/set/tuple/primitive)
    """
    
    # ANSI color escape codes
    RESET = "\033[0m"  # Resets all styling
    
    # Color assignments
    INDEX_COLOR = "\033[38;5;245m"  # Dark grey for indices/type text
    PAREN_COLOR = "\033[33m"        # Yellow for parentheses 
    KEY_COLOR = "\033[38;5;250m"    # Light grey for dictionary keys
    VALUE_COLOR = "\033[96m"        # Light blue for values
    ARROW_COLOR = "\033[37m"        # White for arrow
    
    # Depth-based connector colors (rotates through these)
    CONNECTOR_COLORS = [
        "\033[36m",  # cyan
        "\033[35m",  # magenta
        "\033[32m",  # green
        "\033[34m",  # blue
        "\033[31m"   # red
    ]
        
    def _print_recursive(data: Any, indent: int = 0, is_last_list: Optional[List[bool]] = None, parent_index: str = "") -> None:
        
        """
        Recursive helper function that handles the actual printing.
        
        Args:
            data: Current data node to process
            indent: Current depth level (for indentation)
            is_last_list: Stack tracking whether parent nodes were last in their containers
            parent_index: String index path (e.g. "0.2.1")
        """
        if is_last_list is None:
            is_last_list = []
        
        # Get connector color for current depth
        line_color = CONNECTOR_COLORS[indent % len(CONNECTOR_COLORS)]
        
        # Build the indentation prefix
        prefix = ""
        for level in range(indent):
            if level < len(is_last_list) and not is_last_list[level]:
                prefix += f"{CONNECTOR_COLORS[level % len(CONNECTOR_COLORS)]}│   {RESET}"
            else:
                prefix += "    "
        
        # Handle dictionaries
        if isinstance(data, dict):
            items = data.items()
            for i, (key, value) in enumerate(items):
                is_last = (i == len(items) - 1)
                connector = f"{line_color}╰── {RESET}" if is_last else f"{line_color}├── {RESET}"
                current_index = f"{parent_index}{i}."
                
                # Format all display components
                colored_index = f"{INDEX_COLOR}{current_index.rstrip('.')}{RESET}"
                colored_key = f"{KEY_COLOR}{key}{RESET}"
                type_str = f"{PAREN_COLOR}({INDEX_COLOR}{type(value).__name__}{PAREN_COLOR}){RESET}"
                arrow = f"{ARROW_COLOR} ▶ {RESET}"
                
                if isinstance(value, (dict, list, set, tuple)):
                    print(f"{prefix}{connector}{colored_index} {colored_key} {type_str}")
                    _print_recursive(value, indent + 1, is_last_list + [is_last], current_index)
                else:
                    colored_value = f"{VALUE_COLOR}{value}{RESET}"
                    print(f"{prefix}{connector}{colored_index} {colored_key} {type_str}{arrow}{colored_value}")
        
        # Handle sequences (list/set/tuple)
        elif isinstance(data, (list, set, tuple)):
            for i, value in enumerate(data):
                is_last = (i == len(data) - 1)
                connector = f"{line_color}╰── {RESET}" if is_last else f"{line_color}├── {RESET}"
                current_index = f"{parent_index}{i}."
                
                colored_index = f"{INDEX_COLOR}{current_index.rstrip('.')}{RESET}"
                
                # Improved type display for classes and functions
                if inspect.isclass(value):
                    type_str = f"{PAREN_COLOR}({INDEX_COLOR}class: {value.__name__}{PAREN_COLOR}){RESET}"
                elif inspect.isfunction(value):
                    type_str = f"{PAREN_COLOR}({INDEX_COLOR}function: {value.__name__}{PAREN_COLOR}){RESET}"
                else:
                    type_str = f"{PAREN_COLOR}({INDEX_COLOR}{type(value).__name__}{PAREN_COLOR}){RESET}"
                
                arrow = f"{ARROW_COLOR} ▶ {RESET}"
                
                if isinstance(value, (dict, list, set, tuple)):
                    print(f"{prefix}{connector}{colored_index} {type_str}")
                    _print_recursive(value, indent + 1, is_last_list + [is_last], current_index)
                else:
                    colored_value = f"{VALUE_COLOR}{value}{RESET}"
                    print(f"{prefix}{connector}{colored_index} {type_str}{arrow}{colored_value}")
        
        # Handle primitive values (fallback)
        else:
            connector = f"{line_color}╰── {RESET}"
            
            # Improved type display for classes and functions
            if inspect.isclass(data):
                type_str = f"{PAREN_COLOR}({INDEX_COLOR}class: {data.__name__}{PAREN_COLOR}){RESET}"
            elif inspect.isfunction(data):
                type_str = f"{PAREN_COLOR}({INDEX_COLOR}function: {data.__name__}{PAREN_COLOR}){RESET}"
            else:
                type_str = f"{PAREN_COLOR}({INDEX_COLOR}{type(data).__name__}{PAREN_COLOR}){RESET}"
            
            arrow = f"{ARROW_COLOR} ▶ {RESET}"
            colored_value = f"{VALUE_COLOR}{data}{RESET}"
            print(f"{prefix}{connector}{type_str}{arrow}{colored_value}")

    # Start the recursive printing with default values
    _print_recursive(data)


# Help message for command-line usage
HELP_MESSAGE = """
Nested Data Structure Visualizer

Usage:
    print_tree(data)

Features:
- Color-coded hierarchical display
- Shows data types in yellow parentheses
- Index path for each element (e.g. "0.2.1")
- Supports dictionaries, lists, sets, tuples and primitives

Color Legend:
    Grey: Indices and type names
    Yellow: Parentheses showing type
    Light Grey: Dictionary keys  
    Light Blue: Values
    White: Arrow symbol
    Rotating Colors: Connector lines (changes per depth level)

Example:
    data = {
        "user": {
            "name": "Alice",
            "scores": [95, 88, 72]
        }
    }
    print_tree(data)
"""

# Make help accessible through help()
print_tree.__doc__ = HELP_MESSAGE