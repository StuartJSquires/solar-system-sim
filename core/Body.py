from itertools import chain, imap

class Body(object):
    """This is the class used for all bodies affected by gravity.

    Attributes:
        name: the name of the body
        position: a numpy array representing the position vector in 3D Cartesian
            coordinates
        velocity: a numpy array representing the velocity vector in 3D Cartesian
            coordinates
    """

    def __init__(self, name, position, velocity):
        """This constructs a body with a name, position, and velocity

        Args:
            name: the name of the body
            position: a numpy array representing the position vector in 3D 
            Cartesian coordinates
            velocity: a numpy array representing the velocity vector in 3D 
            Cartesian coordinates
        """

        self.name = name
        self.position = position
        self.velocity = velocity

    def __iter__(self):
        """Implement the iterator protocol.
        """
        if self.children is not None:
            for body in chain(*imap(iter, self.children)):
                yield body

        yield self


class MassiveBody(Body):
    """This is the class used for all bodies affected by gravity.

    Attributes:
        name: the name of the body
        position: a numpy array representing the position vector in 3D Cartesian
            coordinates
        velocity: a numpy array representing the velocity vector in 3D Cartesian
            coordinates
        mass: the mass of the body in kilograms
    """

    def __init__(self, name, position, velocity, mass):
        """This constructs a body with a name, position, velocity, and mass
        Args:
            name: the name of the body
            position: a numpy array representing the position vector in 3D 
            Cartesian coordinates
            velocity: a numpy array representing the velocity vector in 3D 
            Cartesian coordinates
            mass: the mass of the body in kilograms
        """

        super().__init__(name, position, velocity)
        self.mass = mass