from read_input import *

class Body(object):
    """This is the class used for all bodies. We might want to make subclasses
    for different types of bodies at some point in the future.

    Attributes:
        name: the name of the body
        parent: the name of the body that the orbital parameters of this body 
            are given relative to
        mass: the mass of the body
    """

    def __init__(self, filename):
        """This function takes the list of body parameters from the input files
        and uses them to create the body object with appropriate attributes.

        Args:
            filename: the name of the input file to use to create the body
        """

        body_params = read_body(filename)

        self.name = body_params["name"]
        self.parent = body_params["parent"]
        self.mass = body_params["mass"]