import os

from parameters import *
from class_definitions import System

def main():
    """This is the main function (for now). Runs a simulation with the
    parameters given in parameters.py
    """

    # Pack arguments into a dictionary
    params = {"INITIAL_CONDITION_DIRECTORY": INITIAL_CONDITION_DIRECTORY,
              "OUTPUT_DIRECTORY": OUTPUT_DIRECTORY,
              "OUTPUT_FILE_BASE": OUTPUT_FILE_BASE,
              "BEGIN_TIME": BEGIN_TIME,
              "MAX_TIME": MAX_TIME,
              "MAX_TIME_STEP": MAX_TIME_STEP,
              "OUTPUT_TIME_STEP": OUTPUT_TIME_STEP,
              "TIME_OF_FIRST_OUTPUT": TIME_OF_FIRST_OUTPUT,
              "GRAVITATIONAL_CONSTANT": GRAVITATIONAL_CONSTANT}

    # Initialize the system
    input_dir = os.path.join("input_data", 
                             params["INITIAL_CONDITION_DIRECTORY"])

    main_system = System(input_dir, **params)

    print main_system.members


if __name__ == "__main__":
    main()