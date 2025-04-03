# Python Data Tree Visualizer

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A powerful ANSI-colored tree visualization tool for nested Python data structures.

## Features

- 🎨 **Color-coded output** for easy differentiation of data types
- 🌳 **Hierarchical display** of complex nested structures
- 🔍 **Type information** shown for all elements
- 📊 **Index numbering** for easy navigation
- 🏷️ **Custom formatting** for special Python objects
- 🚀 **Supports** all standard Python types plus custom classes

## Installation

```bash
git clone https://github.com/okhtaymp/python-data-tree.git
cd python-data-tree
```

## Usage

```python
from datatree import print_tree

data = {
    "name": "Test",
    "values": [1, 2, 3],
    "nested": {
        "key": "value",
        "status": True
    }
}

print_tree(data)
```
## Example Output

<pre><font color="#00AAAA">├── </font><font color="#8A8A8A">0</font> <font color="#BCBCBC">name</font> <font color="#AA5500">(</font><font color="#8A8A8A">str</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">Test</font>
<font color="#00AAAA">├── </font><font color="#8A8A8A">1</font> <font color="#BCBCBC">values</font> <font color="#AA5500">(</font><font color="#8A8A8A">list</font><font color="#AA5500">)</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">├── </font><font color="#8A8A8A">1.0</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">1</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">├── </font><font color="#8A8A8A">1.1</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">2</font>
<font color="#00AAAA">│   </font><font color="#AA00AA">╰── </font><font color="#8A8A8A">1.2</font> <font color="#AA5500">(</font><font color="#8A8A8A">int</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">3</font>
<font color="#00AAAA">╰── </font><font color="#8A8A8A">2</font> <font color="#BCBCBC">nested</font> <font color="#AA5500">(</font><font color="#8A8A8A">dict</font><font color="#AA5500">)</font>
    <font color="#AA00AA">├── </font><font color="#8A8A8A">2.0</font> <font color="#BCBCBC">key</font> <font color="#AA5500">(</font><font color="#8A8A8A">str</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">value</font>
    <font color="#AA00AA">╰── </font><font color="#8A8A8A">2.1</font> <font color="#BCBCBC">status</font> <font color="#AA5500">(</font><font color="#8A8A8A">bool</font><font color="#AA5500">)</font><font color="#AAAAAA"> ▶ </font><font color="#55FFFF">True</font>
</pre>

###  click -> [Advanced example](example.md)


## Type Support Matrix 🔢

| Category       | Supported Types                  | Special Features              |
|----------------|----------------------------------|-------------------------------|
| **Primitives** | `int`, `float`, `str`, `bool`    | Value highlighting            |
| **Containers** | `list`, `dict`, `set`, `tuple`   | Size indicators               |
| **Callables**  | Functions, methods, lambdas      | Qualified name display        |
| **Objects**    | Classes, instances               | Attribute summary             |
| **Special**    | `bytes`, `range`, exceptions     | Custom representations       |


## Requirements

- Python 3.10+
- Terminal with ANSI color support

## Contributing 🤝

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.


## License 📜

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
