import json
from os import path

def create_body_template():
    template_file = open(path.join("input_data", "body_template.json"), 'w')
    properties = {'name': "planet",
                  'mass': 0.0, 
                  'semimajor': 0.0, 
                  'eccentricity': 0.0,
                  'azimuthal_angle': 0.0}

    properties_json = json.dumps(properties, sort_keys=True, indent=4, 
                                 separators=(',', ': '))
    
    template_file.write(properties_json)
    template_file.close()

create_body_template()