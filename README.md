# AI Tools Lab

A Python project containing **sorting algorithms and reusable utility functions** for learning, practicing, and demonstrating basic programming concepts.

## 📌 Project Description

**AI Tools Lab** is a Python-based project designed to demonstrate common programming utilities and sorting algorithms.

The project currently includes:

- Sorting algorithms such as **Bubble Sort**
- Reusable utility functions
- Simple and beginner-friendly Python code
- Modular files for better code organization

## 📂 Project Structure

```text
AI Tools Lab/
│
├── sorting.py
├── utils.py
└── README.md
```

### Files

- `sorting.py` — Contains sorting algorithm implementations.
- `utils.py` — Contains reusable utility functions.
- `README.md` — Project documentation.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shriyadevi99-arch/ai-tools-lab.git
```

### 2. Navigate to the project directory

```bash
cd ai-tools-lab
```

### 3. Run the Python files

Make sure Python is installed on your system.

```bash
python sorting.py
```

or

```bash
python utils.py
```

## 🚀 Usage

### Example 1: Bubble Sort

The `sorting.py` file contains a Bubble Sort implementation:

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [64, 34, 25, 12, 22, 11, 90]

print("Sorted list:", bubble_sort(numbers))
```

**Output:**

```text
Sorted list: [11, 12, 22, 25, 34, 64, 90]
```

### Example 2: Utility Functions

The `utils.py` file contains the following utility functions:

- `is_palindrome()` — Checks whether a string is a palindrome.
- `count_words()` — Counts the number of words in a string.
- `celsius_to_fahrenheit()` — Converts Celsius temperature to Fahrenheit.

You can import and use these functions as follows:

```python
from utils import is_palindrome, count_words, celsius_to_fahrenheit

print(is_palindrome("madam"))
print(count_words("Python is easy to learn"))
print(celsius_to_fahrenheit(25))
```

**Output:**

```text
True
5
77.0
```

## 👥 Contributors

- **Shriya Devi** — Project Developer

Contributions, suggestions, and improvements are welcome.

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project, subject to the terms of the MIT License.

See the `LICENSE` file for the complete license text.

---

⭐ **AI Tools Lab** — A simple Python project for learning algorithms, utility functions, and GitHub workflows.