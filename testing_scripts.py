from class_definitions import Body, System

def read_input_test(**params):
    print "Running input test."

    test_system = System("our_solar_system", **params)

    print "List of the bodies in the test system:"

    for body in list(iter(test_system)):
      print body.name

    print "Finished input test."


def timestep_test(**params):
    print "Running timestep test."

    test_system = System("our_solar_system", **params)

    print "Initital positions, velocities, of the bodies:"

    for body in list(iter(test_system)):
        print body.name
        print "position:", body.position
        print "velocity:", body.velocity

    test_system.step(params['MAX_TIME_STEP'], **params)

    print "Positions, velocities, of the bodies at t = ", test_system.time

    for body in list(iter(test_system)):
        print body.name
        print "position:", body.position
        print "velocity:", body.velocity

    print "Finished timestep test."


def many_timestep_test(**params):
    print "Running many timestep test."

    test_system = System("our_solar_system", **params)

    print "Initital positions, velocities, of the bodies:"

    for body in list(iter(test_system)):
        print body.name
        print "position:", body.position
        print "velocity:", body.velocity

    for i in range(10000):
        test_system.step(params['MAX_TIME_STEP'], **params)

    print "Positions, velocities, of the bodies at t = ", test_system.time

    for body in list(iter(test_system)):
        print body.name
        print "position:", body.position
        print "velocity:", body.velocity

    print "Finished many timestep test."


def main():
    test_params = {"OUTPUT_DIRECTORY": "output_directory",
                   "OUTPUT_FILE_BASE": "snapshot",
                   "BEGIN_TIME": 0.0,
                   "MAX_TIME": 1.0,
                   "MAX_TIME_STEP": 100.0,
                   "OUTPUT_TIME_STEP": 0.0,
                   "TIME_OF_FIRST_OUTPUT": 0.0,
                   "INTEGRATOR": 'verlet',
                   "GRAVITATIONAL_CONSTANT": 6.67384 * (10 ** (-11))}

    print "Running test scripts. This may take some time."

    print "----------------------------------------------"
    read_input_test(**test_params)

    timestep_test(**test_params)

    many_timestep_test(**test_params)


if __name__ == "__main__":
    main()