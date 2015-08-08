import sys
import numpy as np
import os

from parameters import params
from class_definitions import System
from data_output import init_output, append_data
from utility_functions import prep_dir

def main():
    print "Initializing..."

    # Unpack parameters
    MAX_TIME = params['MAX_TIME']
    MAX_TIME_STEP = params['MAX_TIME_STEP']
    BEGIN_TIME = params['BEGIN_TIME']
    OUTPUT_TIME_STEP = params['OUTPUT_TIME_STEP']
    INITIAL_CONDITION_DIRECTORY = params['INITIAL_CONDITION_DIRECTORY']
    OUTPUT_DIRECTORY = params['OUTPUT_DIRECTORY']

    END_TIME = MAX_TIME + MAX_TIME_STEP

    system = System(INITIAL_CONDITION_DIRECTORY, **params)

    snapshot_number = 0

    prep_dir(os.path.join("output", OUTPUT_DIRECTORY, "data"))

    init_output(OUTPUT_DIRECTORY, system)
    last_output_time = 0.0

    # Bar step
    last_progressbar_step = 0
    tenth = (MAX_TIME + MAX_TIME_STEP - BEGIN_TIME) / 10.0

    print "Starting simulation:"

    for timestep in np.arange(BEGIN_TIME, END_TIME, MAX_TIME_STEP):
        system.step(MAX_TIME_STEP, **params)

        if system.time >= last_output_time + OUTPUT_TIME_STEP:
            snapshot_number += 1
            append_data(OUTPUT_DIRECTORY, system, snapshot_number)
            last_output_time = system.time
            
        #TODO
        # Progress bar
        if system.time >= last_progressbar_step + tenth:
            print system.time, "/", MAX_TIME
            #sys.stdout.write("#")
            last_progressbar_step = system.time
        

    print "\n"


if __name__ == "__main__":
    main()