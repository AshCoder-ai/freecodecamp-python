def number_pattern(n):
    """
    Generates a space-separated string of numbers from 1 to n.

    Validates that the input is a positive integer before processing.

    Note on Optimization:
    Initially, I accumulated items into a list. I optimized this by
    building the string directly using concatenation inside the for-loop,
    completely removing the need for intermediate list containers.
    """
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    final_string = ""
    for i in range(1, n + 1):
        final_string += str(i) + " "

    return final_string.strip() #Removes the last space
print(number_pattern(6))