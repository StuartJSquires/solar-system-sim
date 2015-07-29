import numpy as np
import pandas as pd
import os

def init_dataframes(system, snapshot_number=0):
    """Initializes the dataframe objects.

    Args:
        system: a System object

    Returns:
        dataframes: a dictionary containing the dataframe objects indexed by the
            body names
    """

    column_names = ['time', 
                    'x_pos', 
                    'y_pos', 
                    'z_pos', 
                    'x_vel', 
                    'y_vel', 
                    'z_vel']

    dataframes = {}

    for body in list(iter(system)):
        initial_data = np.concatenate([np.array([system.time]), 
                                       body.position, 
                                       body.velocity])

        dataframes[body.name] = pd.DataFrame(columns = column_names)
        dataframes[body.name].loc[snapshot_number] = initial_data

    return dataframes


def create_csvs(output_dir, dataframes):
    """Creates the csv files from the initial dataframes.

    Args:
        output_dir: the directory used for output in this simulation
        dataframes: the dictionary containing the dateframe objects
    """

    for name in dataframes:
        path = os.path.join("output", output_dir, "data", name + ".csv")
        dataframes[name].to_csv(path, mode='w')


def init_output(output_dir, system):
    """Creates the initial csv files from the System object.

    Args:
        output_dir: the directory used for output in this simulation
        system: a System object
    """

    dataframes = init_dataframes(system)
    create_csvs(output_dir, dataframes)

def append_to_csv(output_dir, dataframes):
    """Appends the dataframe info to the csv files.

    Args:
        output_dir: the directory used for output in this simulation
        dataframes: the dictionary containing the dateframe objects
    """

    for name in dataframes:
        path = os.path.join("output", output_dir, "data", name + ".csv")
        with open(path, 'a') as f:
            dataframes[name].to_csv(f, header=False)


def append_data(output_dir, system, snapshot_number):
    """Appends the current system data to the csv files.

    Args:
        output_dir: the directory used for output in this simulation
        system: a System object
    """

    dataframes = init_dataframes(system, snapshot_number)
    append_to_csv(output_dir, dataframes)
