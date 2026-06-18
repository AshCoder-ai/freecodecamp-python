def number_pattern(n):
    """
    Generates a space-separated string of numbers from 1 to n.

    Validates that the input is a positive integer before processing.

    Note on Optimization:
    Initially, I stored integers in a list and used map() afterward.
    I optimized this by converting integers to strings directly inside
    the for-loop to save memory and eliminate the extra map step.
    """
    output = []
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    for i in range(1, n + 1):
        output.append(str(i))

    return " ".join(output)
print(number_pattern(5))