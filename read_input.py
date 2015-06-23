import json
from os import path

def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii') if isinstance(x, unicode) else x
    return dict(map(ascii_encode, pair) for pair in data.items())


def read_body(filename):
    """Reads the body information from a file in input_data and creates a 
    dictionary.

    Args:
        filename: the name of the file to read_body

    Returns:
        body_info: a dictionary containing information for the body
    """

    body_file = open(filename, 'r')
    body_json = body_file.read()

    body_info = json.loads(body_json, object_hook = ascii_encode_dict)

    return body_info