from class_definitions import Body, System

def read_input_test(**params):
    test_system = System("our_solar_system", **params)
    for member in test_system.members:
        print member.name
        for child in member.children:
            print child.name
            print "position", child.position


def main():
    test_params = {"OUTPUT_DIRECTORY": "output_directory",
                   "OUTPUT_FILE_BASE": "snapshot",
                   "BEGIN_TIME": 0.0,
                   "MAX_TIME": 0.0,
                   "MAX_TIME_STEP": 0.0,
                   "OUTPUT_TIME_STEP": 0.0,
                   "TIME_OF_FIRST_OUTPUT": 0.0,
                   "GRAVITATIONAL_CONSTANT": 6.67384 * (10 ** (-11))}

    read_input_test(**test_params)


if __name__ == "__main__":
    main()