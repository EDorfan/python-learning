"""
Lists in Python: explanation, examples, edge cases, practice, and a fix-it.

What is a list?
- A list is an ordered, mutable sequence. Use it to store items in order, modify them,
  and iterate over them. Lists can hold mixed types (ints, strings, other lists, etc.).
- Syntax: [] for literal, list(iterable) to build from any iterable.

Key properties:
- Ordered: preserves insertion order.
- Mutable: you can reassign, append, extend, insert, remove, sort, etc.
- Indexable and sliceable: positive and negative indices, slices create shallow copies.
- Heterogeneous: items can be any Python object.

This file is runnable. Explore examples in the __main__ block at the bottom.
Practice: Implement the function skeleton(s) in the Practice section.
Fix-it: There is a purposely broken example (commented tests) you can fix.
"""

from __future__ import annotations
from copy import deepcopy
from typing import Iterable, List


def basics_examples() -> None:
    """Show core list behaviors: creation, indexing, slicing, and mutability."""
    # Creation
    empty = []
    numbers = [10, 20, 30, 40]
    mixed = [1, "two", 3.0, [4, 5]]
    from_iterable = list(range(3))  # [0, 1, 2]

    print("Creation:", empty, numbers, mixed, from_iterable)

    # Indexing (0-based) and negative indexing
    print("Indexing:", numbers[0], numbers[-1])  # 10, 40

    # Slicing: [start:end:step] produces a shallow copy
    print("Slicing:", numbers[1:3], numbers[:], numbers[::-1])

    # Mutability: reassign, append, extend, insert, remove, pop
    nums = numbers[:]  # copy to keep original intact below
    nums[1] = 25
    nums.append(50)  # add one item
    nums.extend([60, 70])  # add many
    nums.insert(0, 5)  # insert at index
    removed = nums.pop()  # remove and return last (70)
    nums.remove(25)  # remove first occurrence of value
    print("Mutated list:", nums, "removed=", removed)


def methods_examples() -> None:
    """Demonstrate useful methods: count, index, sort, reverse, clear."""
    data = [3, 1, 2, 3, 2, 3]
    print("Count of 3:", data.count(3))  # 3
    print("Index of first 2:", data.index(2))  # 2

    # Sorting in place vs. producing a new sorted list
    copy_for_sort = data[:]
    copy_for_sort.sort()  # in-place
    print("Sorted in place:", copy_for_sort)

    descending = sorted(data, reverse=True)  # new list
    print("Sorted (new list, desc):", descending)

    # Custom sort using key
    words = ["pear", "apple", "banana", "fig"]
    words_sorted_by_length = sorted(words, key=len)
    print("Sorted by length:", words_sorted_by_length)

    # Reverse in place
    words.reverse()
    print("Reversed:", words)

    # Clear all items
    tmp = [1, 2, 3]
    tmp.clear()
    print("Cleared list:", tmp)


def copying_and_aliasing() -> None:
    """Show the difference between aliasing and copying (shallow vs deep)."""
    original = [[1, 2], [3, 4]]
    alias = original  # no copy; both names point to same list
    shallow = original[:]  # shallow copy (top-level list only)
    deep = deepcopy(original)  # deep copy (recursively copies nested lists)

    alias[0][0] = 999
    print("After alias mutation:")
    print("original:", original)  # mutated because alias shares inner lists
    print("shallow:", shallow)    # also sees inner mutation (shallow copy shares inner lists)
    print("deep:", deep)          # unchanged


def comprehensions_examples() -> None:
    """List comprehensions: concise list building with optional conditions."""
    squares = [n * n for n in range(6)]
    evens = [n for n in range(10) if n % 2 == 0]
    cartesian_pairs = [(x, y) for x in range(2) for y in range(3)]
    print("Comprehensions:", squares, evens, cartesian_pairs)


def edge_cases_examples() -> None:
    """Edge cases and pitfalls with safe demonstrations (exceptions shown via comments)."""
    # Empty list operations
    empty: List[int] = []
    print("Empty length:", len(empty))
    print("Membership on empty:", 1 in empty)
    # Accessing empty[0] would raise IndexError
    # empty[0]

    # Negative indices
    nums = [1, 2, 3]
    print("Negative index -1:", nums[-1])  # 3

    # Slices are forgiving and never raise IndexError
    print("Slice beyond bounds:", nums[10:20])  # []

    # Removing a non-existent item raises ValueError
    # nums.remove(999)  # ValueError: list.remove(x): x not in list

    # Sorting with incomparable mixed types raises TypeError in Python 3
    mixed = [1, 2, "three"]
    # sorted(mixed)  # TypeError in Python 3
    print("Mixed types present (sorting would fail):", mixed)

    # Common pitfall: list multiplication with nested lists (aliasing rows)
    bad_grid = [[0] * 3] * 3  # all rows reference the same inner list
    bad_grid[0][0] = 1
    print("Bad grid (aliasing):", bad_grid)  # first column all 1s

    good_grid = [[0 for _ in range(3)] for _ in range(3)]
    good_grid[0][0] = 1
    print("Good grid (independent rows):", good_grid)


# Practice: Implement this function
def unique_sorted_even_numbers(nums: Iterable[int]) -> list[int]:
    """Return unique even numbers from nums, sorted ascending.

    Examples
    --------
    unique_sorted_even_numbers([5, 2, 8, 2, 7, 4]) -> [2, 4, 8]
    unique_sorted_even_numbers([]) -> []

    Your task: implement using list tools (comprehensions, set, or loops).
    For practice, start with a comprehension and sorted().
    """
    # TODO: Replace the implementation below with your own.
    # Tip: A straightforward approach is: filter evens -> use set for uniqueness -> sorted
    evens = [n for n in nums if isinstance(n, int) and n % 2 == 0]
    return sorted(set(evens))


# Broken example for you to fix (do not execute by default)
def remove_all_bad(items: list[int], value: int) -> list[int]:
    """BUGGY: Attempts to remove all occurrences of value but skips some.

    The classic bug is mutating a list while iterating over it in-place.
    For example, removing items as you traverse forward causes index shifting
    and skipped items.

    Try this in the REPL or by uncommenting the failing test in __main__:
        remove_all_bad([1, 2, 2, 2, 3], 2)  # often returns [1, 2, 3], not [1, 3]
    """
    for i, x in enumerate(items):
        if x == value:
            items.pop(i)  # BUG: index shifts left, next element skipped
    return items


def remove_all_good(items: list[int], value: int) -> list[int]:
    """Correct approach: build a new list or iterate backward safely."""
    # Build a new list with a comprehension (simple and efficient):
    return [x for x in items if x != value]

    # Alternative safe in-place removal (iterate backwards):
    # for i in range(len(items) - 1, -1, -1):
    #     if items[i] == value:
    #         items.pop(i)
    # return items


def run_all_examples() -> None:
    basics_examples()
    methods_examples()
    copying_and_aliasing()
    comprehensions_examples()
    edge_cases_examples()


if __name__ == "__main__":
    print("\n--- List Tutorial Examples ---")
    run_all_examples()

    print("\n--- Practice: unique_sorted_even_numbers ---")
    practice_input = [5, 2, 8, 2, 7, 4, 10, 10, -2, 0]
    print("Input:", practice_input)
    print("Output:", unique_sorted_even_numbers(practice_input))

    # Fix-it: Broken example (commented out so the file runs cleanly).
    # Uncomment to see failing behavior, then fix remove_all_bad.
    # print("\n--- Fix-it: remove_all_bad vs remove_all_good ---")
    # buggy_result = remove_all_bad([1, 2, 2, 2, 3], 2)
    # print("Buggy result:", buggy_result)  # likely [1, 2, 3]
    # correct_result = remove_all_good([1, 2, 2, 2, 3], 2)
    # print("Correct result:", correct_result)  # [1, 3]


