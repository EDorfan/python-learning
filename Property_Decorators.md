# **Python Property Decorators — Summary**

*Based on Corey Schafer’s Python OOP Tutorial (Video 9)*

---

## **1. Introduction**

In Python, **property decorators** allow you to manage **class attributes** more **cleanly and safely** without changing how users interact with your class.

Traditionally, you'd call methods to **get** or **set** attributes, but with property decorators, you can use **methods like attributes** — making your code **cleaner, more intuitive, and less error-prone**.

---

## **2. The Problem**

Suppose you create a class to represent employees:

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
```

**Issue:**
If we later update the `first` or `last` name, the `email` won't automatically update.

```python
emp_1 = Employee('John', 'Doe')
print(emp_1.email)    # john.doe@email.com

emp_1.first = 'Corey'
print(emp_1.email)    # ❌ Still prints john.doe@email.com
```

We need a better solution — and **property decorators** provide it.

---

## **3. Using `@property`**

We can make `email` **calculate dynamically** instead of hardcoding it.

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"
```

Now, even if we change `first` or `last`, the `email` updates automatically:

```python
emp_1 = Employee('John', 'Doe')
print(emp_1.email)    # john.doe@email.com

emp_1.first = 'Corey'
print(emp_1.email)    # corey.doe@email.com ✅
```

**Benefit:**
We can **call `emp_1.email` like an attribute**, not a method.
If we didn’t use `@property`, we'd have to do `emp_1.email()` instead.

---

## **4. Adding a Setter (`@<property>.setter`)**

Sometimes, you want to **update multiple attributes** when one is changed.
For example, if we update an employee's **full name**, we want **both** `first` and `last` to change.

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
```

**Usage:**

```python
emp_1 = Employee('John', 'Doe')

emp_1.fullname = "Corey Schafer"
print(emp_1.first)     # Corey
print(emp_1.last)      # Schafer
print(emp_1.email)     # corey.schafer@email.com ✅
```

---

## **5. Adding a Deleter (`@<property>.deleter`)**

We can define what happens when someone **deletes** an attribute:

```python
@fullname.deleter
def fullname(self):
    print("Delete Name!")
    self.first = None
    self.last = None
```

**Usage:**

```python
del emp_1.fullname
# Output: Delete Name!
print(emp_1.first)   # None
print(emp_1.last)    # None
```

---

## **6. How the Provided Code Works**

Your code combines **all three decorators**:

* `@property` → Lets you **access email and fullname like attributes**
* `@fullname.setter` → Lets you **update fullname** and automatically change `first`, `last`, and `email`
* `@fullname.deleter` → Defines what happens when fullname is deleted

---

## **7. Real-World Use Cases**

### **Example 1 — Employee Management System** ✅ *(Most relevant)*

If you have hundreds of employees, you want **email, ID, and usernames** to automatically stay consistent when someone’s name changes.

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def username(self):
        return f"{self.first[0].lower()}{self.last.lower()}"
```

This ensures that updating an employee’s name **automatically updates** everything else.

---

### **Example 2 — Financial Systems**

Imagine a stock trading app where **account balance** is derived from transactions:

```python
class Account:
    def __init__(self, deposits, withdrawals):
        self.deposits = deposits
        self.withdrawals = withdrawals

    @property
    def balance(self):
        return sum(self.deposits) - sum(self.withdrawals)
```

If deposits or withdrawals change, `balance` updates instantly — **no need to manually recalculate**.

---

### **Example 3 — Data Validation**

Using setters, we can enforce rules automatically:

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
```

Now, invalid updates are blocked:

```python
p = Product(100)
p.price = -50   # ❌ Raises ValueError
```

---

## **8. Key Takeaways**

| **Decorator**     | **Purpose**                                   | **Access Example**          |
| ----------------- | --------------------------------------------- | --------------------------- |
| `@property`       | Makes a method act like an **attribute**      | `emp.email`                 |
| `@<prop>.setter`  | Lets you **set** a derived attribute          | `emp.fullname = "New Name"` |
| `@<prop>.deleter` | Defines behavior when an attribute is deleted | `del emp.fullname`          |

---

## **9. Best Practices**

* ✅ Use `@property` for **calculated attributes**
* ✅ Use setters only when needed — otherwise, keep attributes **read-only**
* ✅ Use deleters sparingly — often better to handle cleanup explicitly
* ✅ Keep property methods lightweight — avoid heavy computations

---

## **10. Summary**

Property decorators let you:

* Treat **methods like attributes** → cleaner API
* Keep attributes **in sync** automatically
* Enforce **validation and constraints**
* Avoid **breaking existing code** when refactoring
