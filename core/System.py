from itertools import chain, imap

#   Define Gravitational constant
G = 6.67384 * (10 ** (-11))


class System():
    """A system is a collection of bodies/subsystems.

    Attributes:
        members: the list of members of the system
        time: the global time in seconds
        integrator: the type of numerical integrator to use
    """

    def __init__(self, start_time):
        """This function should initialize a system given its directory name.

        Args: 
            start_time: the initial time of the system
        """

        # Initialize the time
        self.time = start_time

        # Initialize the top level body list
        self.members = []

        self.integrator = integrator

    def __iter__(self):
        """Implement the iterator protocol
        """
        for body in chain(*imap(iter, self.members)):
            yield body
    
    def step(self, timestep):
        """This function updates the system over a timestep using numerical 
        integration.

        Args:
            timestep: the time to step forward in seconds
        """
        if self.integrator == 'verlet':
            self.__verlet_step(timestep, **params)

        self.time += timestep


    def __verlet_step(self, timestep):
        """Steps the system forward by timestep with verlet integration.

        Args:
            timestep: the time to step forward in seconds
        """

        for body in list(iter(self)):
            body.position += body.velocity * timestep / 2.0

        for body in list(iter(self)):
            body.sum_of_accelerations = np.zeros(3)

            for interacting_body in list(iter(self)):
                if interacting_body is not body:
                    distance = body.position - interacting_body.position
                    acceleration = -(G * interacting_body.mass * distance / 
                                     (np.linalg.norm(distance) ** 3.0))
                    body.sum_of_accelerations += acceleration

        for body in list(iter(self)):
            body.velocity += body.sum_of_accelerations * timestep
            body.position += body.velocity * timestep / 2.0