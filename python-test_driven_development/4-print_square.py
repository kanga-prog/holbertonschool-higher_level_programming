def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
    size (int): The size of the square.

    Raises:
    TypeError: If size is not an integer or is a negative float.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):  # Check if size is an integer
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if size == 0:
        return  # No output for size 0

    for _ in range(size):
        print("#" * size)
