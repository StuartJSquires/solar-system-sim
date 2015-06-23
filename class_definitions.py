from read_input import read_body
import numpy as np
import os


class Body(object):
    """This is the class used for all bodies. We might want to make subclasses
    for different types of bodies at some point in the future.

    Attributes:
        name: the name of the body
        parent: the name of the body that the orbital parameters of this body 
            are given relative to
        mass: the mass of the body
    """

    def __init__(self, filename, **params):
        """This function takes the list of body parameters from the input files
        and uses them to create the body object with appropriate attributes.

        Args:
            filename: the name of the input file to use to create the body
        """

        G = params["GRAVITATIONAL_CONSTANT"]
        body_params = read_body(filename)

        self.name = body_params["name"]
        self.parent = body_params["parent"]
        self.mass = body_params["mass"]

        if self.parent is not None:
            self.semimajor = body_params["semimajor"]
            self.eccentricity = body_params["eccentricity"]
            self.argument_of_periapsis = body_params["argument_of_periapsis"]
            self.inclination = body_params["inclination"]
            self.ascending_node_longitude = body_params["ascending_node_longitude"]
            self.direction = body_params["direction"]
            self.start = body_params["start"]

        if self.parent == None:
            self.velocity = np.zeros(3)
            self.position = np.zeros(3)
        else:
            a = self.semimajor
            e = self.eccentricity

            if self.start == "periapsis":
                velocity_magnitude = np.sqrt(((1 + e) * G * M) / ((1 - e) * a))
                position_magnitude = a * (1 - e)
            elif self.start == "apoapsis":
                velocity_magnitude = np.sqrt(((1 - e) * G * M) / ((1 + e) * a))
                position_magnitude = a * (1 + e)
            else:
                print "FATAL ERROR: INVALID START POSITION FOR", self.name
                sys.exit("Stopping program.")

            angle_1 = self.ascending_node_longitude
            angle_2 = self.inclination
            angle_3 = self.argument_of_periapsis

            position_x_direction = ((np.cos(angle_1) * 
            						 np.cos(angle_2) * 
            						 np.cos(angle_3)) - 
            						(np.sin(angle_1) * 
            						 np.sin(angle_2)))

            position_y_direction = ((np.cos(angle_1) * 
            						 np.sin(angle_3)) +
            						(np.cos(angle_2) *
            						 np.cos(angle_3) *
            						 np.sin(angle_1)))

            position_z_direction = np.cos(angle_3) * np.sin(angle_2)

            position_direction = np.asarray([position_x_direction,
            								 position_y_direction,
            								 position_z_direction])

            self.position = position_magnitude * position_direction

            velocity_x_direction = (-(np.cos(angle_3) * 
            						  np.sin(angle_1)) -
            						(np.cos(angle_1) *
            						 np.cos(angle_2) *
            						 np.sin(angle_3)))

            velocity_y_direction = ((np.cos(angle_1) * 
            						 np.cos(angle_3)) -
            						 np.cos(angle_2) * 
            						 np.sin(angle_1) *
            						 np.sin(angle_3))

            velocity_z_direction = -np.sin(angle_2) * np.sin(angle_3)

            velocity_direction = np.asarray([velocity_x_direction,
            								 velocity_y_direction,
            								 velocity_z_direction])

            self.velocity = velocity_magnitude * position_magnitude


class System():
    """A system is a collection of bodies/subsystems.

    Attributes:
        members: the list of members of the system
    """

    def __init__(self, directory_name, **params):
        members = []

        for filename in os.listdir(directory_name):
            file_path = os.path.join(directory_name, filename)
            members.append(Body(file_path, **params))
