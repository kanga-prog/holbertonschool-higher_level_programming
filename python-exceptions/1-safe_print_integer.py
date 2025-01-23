def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True  # Return True if printing is successful
    except (ValueError, TypeError):
        return False  # Return False if an error occurs


def safe_print_integer(value):
    try:
        # Essayer de convertir la valeur en entier
        print("{:d}".format(int(value)))
        return True  # Si la conversion et l'impression réussissent, retourner True
    except (ValueError, TypeError):
        # Si la conversion échoue, attraper les erreurs et retourner False
        return False
