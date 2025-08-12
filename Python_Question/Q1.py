'''Write a Python function to check whether a number is in a given range. '''


def is_in_range(number, start, end):
    
    return start <= number <= end

if __name__ == "__main__":
    # Test cases
    test_numbers = [5, 15, 0, -3, 10]
    range_start = 1
    range_end = 10

    for num in test_numbers:
        result = is_in_range(num, range_start, range_end)
        print(f"Is {num} in range {range_start} to {range_end}? {result}")
