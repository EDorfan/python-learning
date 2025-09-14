# **Python OOP Tutorial 5: Special (Magic/Dunder) Methods**

This tutorial explains **special methods** (also called **magic methods** or **dunder methods**) in Python. These are built-in hooks that allow us to **customize the behavior of objects** for built-in operations like addition, printing, length, comparisons, and more.

---

## **🎥 Video Summary**

* **Magic methods** are Python methods **wrapped in double underscores**:
  e.g. `__init__`, `__add__`, `__len__`, `__str__`.
* Python invokes these methods **implicitly**:

  * `a + b` → calls `a.__add__(b)`
  * `len(a)` → calls `a.__len__()`
* By defining these methods in your classes, you can make **custom objects behave like built-in types**.

---

## **📌 Common Magic Methods**

| **Method**                   | **Purpose**                                                            |
| ---------------------------- | ---------------------------------------------------------------------- |
| `__init__`                   | Initializes a new instance.                                            |
| `__str__`                    | Human-readable string representation of an object (used by `print()`). |
| `__repr__`                   | Unambiguous representation of an object, often used for debugging.     |
| `__add__`                    | Implements behavior for the `+` operator.                              |
| `__len__`                    | Enables use of `len()` on the object.                                  |
| `__sub__`, `__mul__`, etc.   | Support other arithmetic operations (`-`, `*`, `/`, etc.).             |
| `__eq__`, `__lt__`, `__gt__` | Define behavior for comparison operators (`==`, `<`, `>`, etc.).       |
| `__getitem__`                | Enables index access like `obj[index]`.                                |
| `__iter__` / `__next__`      | Make objects **iterable** in loops.                                    |

---

## **💡 Real-World Examples & Implementations**

### **1. Point Class Using `__add__`**

A simple class to represent **2D coordinates** and support addition:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)
```

**Why useful:**
Makes adding two `Point` objects **intuitive and clean**, without manually writing `p1.x + p2.x`.

---

### **2. Custom Container Using `__len__`, `__getitem__`, and `__str__`**

A custom class that behaves **like a list**:

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        return f"MyList({self.items})"

# Usage
ml = MyList([10, 20, 30])
print(len(ml))   # Output: 3
print(ml[1])     # Output: 20
print(ml)        # Output: MyList([10, 20, 30])
```

**Why useful:**
Gives your custom container **list-like behavior**, enabling `len()`, indexing, and printing.

---

### **3. Money Class Handling Currency Logic**

A more **real-world** example where we model money with **operator overloading** and **comparisons**:

```python
from functools import total_ordering
from decimal import Decimal

@total_ordering
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = Decimal(str(amount))
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Money) or self.currency != other.currency:
            return NotImplemented
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        return (
            isinstance(other, Money) and
            self.currency == other.currency and
            self.amount == other.amount
        )

    def __lt__(self, other):
        if not isinstance(other, Money) or self.currency != other.currency:
            return NotImplemented
        return self.amount < other.amount

    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

    def __repr__(self):
        return f"Money({float(self.amount)}, '{self.currency}')"

# Usage
wallet = Money(100, "USD")
expense = Money(30, "USD")

print(wallet + expense)                # USD 130.00
print(wallet > Money(50, "USD"))       # True
print(wallet == Money(100, "USD"))     # True
```

**Why useful:**

* Enforces **currency consistency**.
* Makes arithmetic intuitive (`wallet + expense`).
* Supports comparisons (`>`, `<`, `==`) safely.

---

## **🚀 Why Magic Methods Matter**

* ✅ Make **custom classes behave like built-in types**
* ✅ Enable **cleaner, more intuitive syntax**
* ✅ Improve **code readability & abstraction**
* ✅ Useful for **domain modeling** — e.g., `Point`, `Money`, `Matrix`, `Inventory`, etc.

---

## **🔹 TL;DR**

* Magic (dunder) methods customize **how objects interact with built-in functions and operators**.
* Examples:

  * `__add__` → object addition
  * `__len__` → `len(obj)`
  * `__str__` / `__repr__` → readable & debug-friendly printing
  * Comparison & arithmetic operations
* **Rule of thumb:** Use them to make your **custom objects intuitive and Pythonic**.

---

Do you want me to make a **complete reference cheat sheet** for **all commonly used dunder methods** — with short explanations and examples?
I can make it compact, visual, and beginner-friendly so you can glance at it whenever you're coding. It’ll be like a one-page guide for magic methods. Should I?
