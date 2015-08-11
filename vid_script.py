import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import os
import subprocess
import seaborn as sns

from vid_parameters import params
from utility_functions import prep_dir, remove_file, ensure_dir


def main():
    SIM_NAME = params["SIM_NAME"]
    VID_NAME = params["VID_NAME"]
    SNAPSHOT_START = params["SNAPSHOT_START"]
    SNAPSHOT_END = params["SNAPSHOT_END"]
    RESOLUTION = params["RESOLUTION"]

    prep_dir(os.path.join("output", SIM_NAME, "tmp"))

    dataframes = load_csv(os.path.join("output", SIM_NAME, "data"))

    # Initialize plot here
    limits = get_limits(dataframes)
    (fig, ax) = init_plot(dataframes, limits, RESOLUTION)

    tenth = (SNAPSHOT_END + 1 - SNAPSHOT_START) / 10

    current_tenth = 0
    
    print "Drawing frames..."

    for snapshot in range(SNAPSHOT_START, SNAPSHOT_END + 1):
        # Update plot here
        fig, ax = update_plot(dataframes, fig, ax, limits, snapshot)

        # Save plot here
        filename = VID_NAME + "%04d.png" % snapshot
        fig.savefig(os.path.join("output", SIM_NAME, "tmp", filename), dpi=120)

        if snapshot == (current_tenth + 1) * tenth:
            current_tenth += 1
            percent = str(current_tenth * 10) + "%"
            print percent, "of frames finished drawing."

    print "All frames finished drawing."
            


    # Delete old mp4 if it exists
    remove_file(os.path.join("output", SIM_NAME, "video", VID_NAME + ".mp4"))

    # Ensure the directory exists
    ensure_dir(os.path.join("output", SIM_NAME, "video"))

    print "\nCreating video from frames..."

    # Create mp4
    create_video_from_frames(SIM_NAME, VID_NAME, fps=60)

    print "\nClearing tmp directory..."

    # Clear snapshot directory
    prep_dir(os.path.join("output", SIM_NAME, "tmp"))

    print "Finished."


def get_datapoints(dataframes, snapshot=0):
    positions = []

    for name in dataframes:
        positions.append(dataframes[name].loc[snapshot])

    xs, ys, zs = [], [], []

    for position in positions:
        xs.append(position['x_pos'])
        ys.append(position['y_pos'])
        zs.append(position['z_pos'])

    return (xs, ys, zs)


def get_limits(dataframes):
    x_lims, y_lims, z_lims = [0.0, 0.0], [0.0, 0.0], [0.06, 0.06]

    for name in dataframes:
        x_min = np.min(dataframes[name]['x_pos'])
        x_max = np.max(dataframes[name]['x_pos'])
        y_min = np.min(dataframes[name]['y_pos'])
        y_max = np.max(dataframes[name]['y_pos'])
        z_min = np.min(dataframes[name]['z_pos'])
        z_max = np.max(dataframes[name]['z_pos'])

        if x_min < x_lims[0]:
            x_lims[0] = x_min
        if x_max > x_lims[1]:
            x_lims[1] = x_max

        if y_min < y_lims[0]:
            y_lims[0] = y_min
        if y_max > y_lims[1]:
            y_lims[1] = y_max

        if z_min < z_lims[0]:
            z_lims[0] = z_min
        if z_max > z_lims[1]:
            z_lims[1] = z_max

    return (x_lims, y_lims, z_lims)


def init_plot(dataframes, limits, resolution):
    x_lims, y_lims, z_lims = limits

    horizontal_size = resolution[0] / 120
    vertical_size = resolution[1] / 120

    fig = plt.figure(figsize = (horizontal_size, vertical_size))
    ax = fig.add_subplot(111, projection = '3d')

    xs, ys, zs = get_datapoints(dataframes)

    ax.scatter(xs, ys, zs)

    ax.grid(b = False)

    ax.set_xlim(x_lims[0], x_lims[1])
    ax.set_ylim(y_lims[0], y_lims[1])
    ax.set_zlim(-0.06, 0.06)

    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')

    return (fig, ax)


def update_plot(dataframes, fig, ax, limits, snapshot):
    x_lims, y_lims, z_lims = limits

    plt.cla()

    xs, ys, zs = get_datapoints(dataframes, snapshot)

    ax.scatter(xs, ys, zs)

    ax.grid(b = False)

    ax.set_xlim(x_lims[0], x_lims[1])
    ax.set_ylim(y_lims[0], y_lims[1])
    ax.set_zlim(-0.06, 0.06)

    return (fig, ax)


def load_csv(data_dir):
    """Loads the data from .csv's and returns the DataFrames

    Args:
        data_dir: the directory the data is contained in

    Returns:
        dataframes: a dictionary containing the DataFrames
    """

    path, dirs, files = os.walk(data_dir).next()

    files = [f for f in files if f.endswith(".csv")]

    dataframes = {}

    for f in files:
        f_path = os.path.join(data_dir, f)
        dataframes[f] = pd.read_csv(f_path)

    return dataframes


def create_video_from_frames(sim_name, vid_name, fps=60):
    """This is slightly hacked together.
    """

    tmp_directory = os.path.join("output", sim_name, "tmp")
    output_directory = os.path.join("output", sim_name, "video")

    command = "avconv -f image2 -r %s -i " % str(fps)
    command += "%s.png" % (os.path.join(tmp_directory, vid_name + "%04d"))
    command += " -c:v libx264 -r 30 %s.mp4" % (os.path.join(output_directory, vid_name))
    print "Running command:"
    print command
    p = subprocess.Popen(command, shell=True, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate()[0]
    print "output\n"+"*"*10+"\n"
    print output
    print "*"*10
    print "Video file has been written"


if __name__ == "__main__":
    main()