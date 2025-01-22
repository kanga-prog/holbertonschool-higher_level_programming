def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True  # Return True if printing is successful
    except (ValueError, TypeError):
        return False  # Return False if an error occurs
