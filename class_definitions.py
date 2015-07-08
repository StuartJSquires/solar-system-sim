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

    def __init__(self, filename, directory_name, parent = None, **params):
        """This function takes the list of body parameters from the input files
        and uses them to create the body object with appropriate attributes.

        Args:
            filename: the name of the input file to use to create the body
        """

        # Get the gravitational constant
        G = params["GRAVITATIONAL_CONSTANT"]

        # Read in the body params
        file_path = os.path.join(directory_name, filename)
        body_params = read_body(file_path)

        self.name = body_params["name"]
        self.parent_name = body_params["parent"] # Note this doesn't do anything
        self.mass = body_params["mass"]

        # Set these parameters only if the body isn't the top level
        if parent is not None:
            self.semimajor = body_params["semimajor"]
            self.eccentricity = body_params["eccentricity"]
            self.argument_of_periapsis = body_params["argument_of_periapsis"]
            self.inclination = body_params["inclination"]
            self.ascending_node_longitude = body_params["ascending_node_longitude"]
            self.direction = body_params["direction"]
            self.start = body_params["start"]

        # If the body is the top level, it's the origin!
        if parent == None:
            self.velocity = np.zeros(3)
            self.position = np.zeros(3)
        else: # Otherwise, we need to initialize the position and velocity
            # These are for shorthand
            a = self.semimajor
            e = self.eccentricity
            M = parent.mass

            # Get the magnitude of the position and velocity
            if self.start == "periapsis":
                velocity_magnitude = np.sqrt(((1 + e) * G * M) / ((1 - e) * a))
                position_magnitude = a * (1 - e)
            elif self.start == "apoapsis":
                velocity_magnitude = np.sqrt(((1 - e) * G * M) / ((1 + e) * a))
                position_magnitude = a * (1 + e)
            else:
                print "FATAL ERROR: INVALID START POSITION FOR", self.name
                sys.exit("Stopping program.")

            # Get angles for rotation transformation
            angle_1 = self.ascending_node_longitude
            angle_2 = self.inclination
            angle_3 = self.argument_of_periapsis

            # Calculate the direction vectors. Hopefully they're unit vectors... 
            # I hope I didn't make a mistake down here! 
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

            # Create position array
            self.position = (position_magnitude * position_direction + 
                             parent.position)

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

            # Create velocity array
            self.velocity = (velocity_magnitude * position_magnitude +
                             parent.velocity)

        # Read in children
        self.children = self.__init_children(directory_name, **params)


    def __init_children(self, directory_name, **params):
        # Get path to children folder
        full_directory_name = os.path.join(directory_name, self.name)

        # Check if children folder exists
        if os.path.isdir(full_directory_name):
            # Init children list
            children = []

            # Walk self.children directory
            path, dirs, files = os.walk(full_directory_name).next()

            if len(files) > 0:
                for filename in files:
                    children.append(Body(filename, full_directory_name, 
                                         self, **params))

                return children
            else:
                print "Directory", full_directory_name, "contains no files."
                return None

        else:
            return None


class System():
    """A system is a collection of bodies/subsystems.

    Attributes:
        members: the list of members of the system
    """

    def __init__(self, directory_name, **params):
        """This function should initialize a system given its directory name.
        """

        # Initialize the top level body list
        self.members = []

        # Walk top directory
        full_directory_name = os.path.join("input_data", directory_name)
        path, dirs, files = os.walk(full_directory_name).next()

        # Make sure there is only one star!
        if len(files) == 1 and len(dirs) == 1:
            self.members.append(Body(files[0], full_directory_name, 
                                parent = None, **params))
        else:
            print "Invalid number of stars or folder structure."
            sys.exit()
