# Task 1: AI-Powered Code Completion - Dictionary Sorting

# Sample data
students = [
    {"name": "Perpetual", "grade": 85, "age": 20},
    {"name": "Steven", "grade": 92, "age": 19},
    {"name": "Onyeka", "grade": 78, "age": 21},
    {"name": "Diana", "grade": 95, "age": 20}
]

# Version 1: AI-Suggested Implementation (Copilot-style)
def sort_dict_list_ai(dict_list, key):
    """Sort a list of dictionaries by a specific key using AI suggestion."""
    return sorted(dict_list, key=lambda x: x[key])

# Version 2: Manual Implementation
def sort_dict_list_manual(dict_list, key, reverse=False):
    """
    Sort a list of dictionaries by a specific key with manual implementation.
    Includes error handling and flexibility.
    """
    if not dict_list:
        return []

    # Validate key exists
    if key not in dict_list[0]:
        raise KeyError(f"Key '{key}' not found in dictionaries")

    # Create a copy to avoid modifying original
    result = dict_list.copy()

    # Sort using key function
    result.sort(key=lambda item: item.get(key, float('inf')), reverse=reverse)

    return result

# Testing both implementations
print("Original list:")
for student in students:
    print(student)

print("\n--- AI Version: Sort by grade ---")
sorted_ai = sort_dict_list_ai(students, "grade")
for student in sorted_ai:
    print(student)

print("\n--- Manual Version: Sort by grade ---")
sorted_manual = sort_dict_list_manual(students, "grade")
for student in sorted_manual:
    print(student)

print("\n--- Manual Version: Sort by grade (descending) ---")
sorted_manual_desc = sort_dict_list_manual(students, "grade", reverse=True)
for student in sorted_manual_desc:
    print(student)

# Performance comparison
import time

large_dataset = [{"id": i, "value": i % 1000} for i in range(10000)]

# Time AI version
start = time.time()
for _ in range(100):
    sort_dict_list_ai(large_dataset, "value")
ai_time = time.time() - start

# Time Manual version
start = time.time()
for _ in range(100):
    sort_dict_list_manual(large_dataset, "value")
manual_time = time.time() - start

print(f"\n--- Performance Comparison (100 iterations on 10,000 items) ---")
print(f"AI Version: {ai_time:.4f} seconds")
print(f"Manual Version: {manual_time:.4f} seconds")
print(f"Difference: {abs(ai_time - manual_time):.4f} seconds")