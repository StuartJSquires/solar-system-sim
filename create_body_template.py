# Run this script to generate a blank json input file in folder "input_files".

import json
from os import path

def create_body_template():
    """Creates a blank JSON template for a generic celestial body."""

    template_file = open(path.join("input_data", "body_template.json"), 'w')
    properties = {'name': "planet",
                  'parent': None,
                  'mass': 0.0, 
                  'semimajor': 0.0, 
                  'eccentricity': 0.0,
                  'ascending_node_longitude': 0.0,
                  'inclination': 0.0,
                  'argument_of_periapsis': 0.0,
                  'direction': "CW",
                  'start': "periapsis"}

    properties_json = json.dumps(properties, sort_keys=True, indent=4, 
                                 separators=(',', ': '))
    
    template_file.write(properties_json)
    template_file.close()


if __name__ == "__main__":
    create_body_template()