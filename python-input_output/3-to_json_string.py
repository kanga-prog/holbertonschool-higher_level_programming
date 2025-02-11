#!/usr/bin/python3

import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne de caractères JSON.

    Args:
        my_obj (object): L'objet Python à convertir en chaîne JSON.

    Returns:
        str: La représentation JSON de l'objet.
    """
    return json.dumps(my_obj)
