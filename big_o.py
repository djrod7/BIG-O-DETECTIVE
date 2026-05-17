import time
import random


# Function A
def get_first(data):
    return data[0]

# O(1) because its single operation 

# Function B
def count_matches(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count

# O(n) because, for item in data:


# Function C
def all_pairs(data):
    pairs = []
    for i in range(len(data)):
        for j in range(len(data)):
            pairs.append((data[i], data[j]))
    return pairs

# O(n²) because for i and for j in range(len(data)):
# There is a nested loop.

# Function D
def mystery(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

# O(log n) because of while n > 1: 
# Its a loop with halving

# Function E
def process(data, target):
    total = sum(data)           # Line 1
    sorted_data = sorted(data)  # Line 2
    first = data[0]             # Line 3
    return total, sorted_data, first

# O(n log n) because sorting. sorted(data)

def count_pairs_nested(data, target):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                count += 1
    return count

def count_pairs_set(data, target):
    count = 0
    seen = set()
    for num in data:
        item = target - num
        if item in seen:
            count += 1
        seen.add(num)
    return count


def benchmark(func, data, target):
    """Time how long a function takes to run."""
    start = time.time()
    result = func(data, target)
    end = time.time()
    return end - start

print("=" * 40)
print("Benchmark")
print("=" * 40)

TARGET = 10
sizes = [1000, 5000, 10000]

print(f"n{'':6} |   Nested: {'':4}  |   Set: {'':6}")
print("-" * 40)

for size in sizes:
    data = random.sample(range(1, size * 10), size)

    t1 = benchmark(count_pairs_nested, data, TARGET)
    t2 = benchmark(count_pairs_set,    data, TARGET)

    print(f"n={size:<6} |   Nested: {t1:.4f}s   |   Set: {t2:.4f}s")
