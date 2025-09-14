## Corey Schafer is King - https://www.youtube.com/watch?v=FsAPt_9Bf3U ##

### **1. What Are Decorators?**

* **Definition:** Decorators are a way to **dynamically add functionality** to functions **without modifying their source code**.
* They “wrap” your original function with extra behavior.
* Useful for:

  * Logging
  * Timing execution
  * Access control
  * Caching results
  * Validation

**Simple idea:**
Take **one function**, **add new functionality**, and **return a new function** — all without changing the original code.

---

### **2. Closures** *(Foundation for Decorators)*

Before decorators, you need to understand **closures** — functions inside functions.

```python
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function("Hi")
bye_func = outer_function("Bye")

hi_func()   # Hi
bye_func()  # Bye
```

* Here, **`outer_function`** returns **`inner_function`**, which remembers the value of `msg` even after `outer_function` has finished.
* This concept of **returning functions that “remember” their context** is essential for decorators.

---

### **3. Basic Function Decorator**

A decorator is just a **function** that takes another function and returns a modified function.

```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function
```

#### Applying the decorator:

**Method 1 – Manual Syntax**

```python
decorated_display = decorator_function(display_original)
decorated_display()
```

**Method 2 – `@` Syntax (Preferred)**

```python
@decorator_function
def display_decorated():
    print("Display function ran")
```

This is equivalent to:
`display_decorated = decorator_function(display_decorated)`

---

### **4. Class-Based Decorators**

You can also create decorators using **classes** with the `__call__` method:

```python
class decorator_class:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call executed before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

@decorator_class
def display_info_1(name, age):
    print(f"Display info ran with arguments ({name}, {age})")

display_info_1("John", 25)
```

* Using a class gives you more flexibility if you need to store **state**.
* However, function decorators are simpler and more common.

---

### **5. Using `*args` and `**kwargs`**

When writing decorators, always include `*args` and `**kwargs` in the wrapper.

* Without them, your decorator would **break** for functions with arguments.

---

### **6. Using `functools.wraps`**

If you decorate a function, Python replaces its metadata (like `__name__` and `__doc__`) with the wrapper’s info.

```python
from functools import wraps

def decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function
```

Without `@wraps`, `display_info.__name__` would become `"wrapper"` instead of `"display_info"`.
This is especially important when **stacking decorators**.

---

### **7. Practical Examples**

#### **a) Logging Decorator**

Writes logs to a file named after the decorated function:

```python
def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f"{original_function.__name__}.log", level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args} and kwargs: {kwargs}")
        return original_function(*args, **kwargs)
    return wrapper
```

---

#### **b) Timer Decorator**

Measures how long a function takes to run:

```python
def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time()
        print(f"{original_function.__name__} ran in: {t2-t1} seconds")
        return result
    return wrapper
```

---

#### **c) Stacking Multiple Decorators**

You can combine decorators:

```python
@my_timer
@my_logger
def display_info_2(name, age):
    print(f"display_info_2 ran with arguments ({name}, {age})")
```

* First, `my_logger` runs.
* Then, `my_timer` wraps the result.
* If you **don’t** use `@wraps`, the `__name__` becomes `"wrapper"` instead of `"display_info_2"`.

---

### **8. Key Takeaways**

| **Concept**            | **Explanation**                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------- |
| **Closure**            | Function inside a function that remembers variables from its enclosing scope.      |
| **Decorator**          | A function/class that adds functionality to another function without modifying it. |
| **`*args`/`**kwargs`** | Ensures decorators work with functions that have varying arguments.                |
| **`functools.wraps`**  | Preserves original function metadata when wrapping functions.                      |
| **Stacking**           | Multiple decorators can wrap the same function, executed from top to bottom.       |
| **Use Cases**          | Logging, timing, validation, caching, authentication, etc.                         |

---

### **Final Example**

```python
@my_timer
@my_logger
def greet(name):
    print(f"Hello {name}")

greet("Eyal")
```

**Output:**

```
Hello Eyal
greet ran in: 0.0002 seconds
```

And `greet.log` will contain:

```
Ran with args: ('Eyal',) and kwargs: {}
```

---

If you want, I can make you a **visual cheat sheet** showing exactly **how decorators wrap functions step by step**.
It would illustrate closures, single decorators, and stacked decorators in one clean diagram — would you like me to make that?
