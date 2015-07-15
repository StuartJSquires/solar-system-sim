import numpy as np
import pandas as pd



def csv_write(dataframe):
    dataframe.to_csv(csv_file_name, mode='w')


def csv_append(file_name, new_data):
    with open(file_name, 'a') as f:
        new_data.to_csv(f, header=False)



column_names = ['x', 'y', 'z']

csv_file_name = 'body_dataframe.csv'

# This is the initial data that will be output
initial_data = np.array([[0.0, 1.0, -1.0]])
# Format to pandas
initial_dataframe = pd.DataFrame(initial_data, columns=column_names)

# This is the data after a timestep
first_timestep_data = np.array([[-0.5, 4.0, -10.1]])
# Format to pandas
first_timestep_dataframe = pd.DataFrame(first_timestep_data, columns=column_names)


def main():

    print
    print 'Initial pandas DataFrame from python'
    print initial_dataframe
    print

    csv_write(initial_dataframe)

    print 'Initial pandas DataFrame read from csv file'
    print pd.read_csv(csv_file_name, index_col=0)
    print
    print 'First timestep DataFrame from python'
    print first_timestep_dataframe
    print

    csv_append(csv_file_name, first_timestep_dataframe)

    print 'csv file after appending first timestep data'
    print pd.read_csv(csv_file_name, index_col=0)
    print


if __name__ == '__main__':
    main()
