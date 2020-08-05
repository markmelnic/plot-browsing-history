
import json
import time
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

DAY = 86400000 # miliseconds

# built histogram dataset
def hist_json(json_file : str, days : int) -> list:
    
    current_time = int(round(time.time() * 1000))
    # read json file
    with open(json_file, mode = 'r', encoding="utf8") as data_file:
        data = json.load(data_file)

    day_nr = 1
    counter = 0
    time_indexes = []
    # process data
    for data_set in data['Browser History']:
        timestamp = round(int(data_set['time_usec']) / 1000)
        if current_time > timestamp:
            time_indexes.append((day_nr, counter))
            day_nr += 1
            counter = 0
            current_time = current_time - DAY
            continue
        counter += 1
        
        if day_nr > days:
            break

    return time_indexes

# generate data histogram
def generate_hist(data : list, days : int):
    
    # separate data
    days_ago = [el[0] for el in data]
    instances = [el[1] for el in data]

    ar_sites = np.arange(len(days_ago))

    # define figure
    fig, ax = plt.subplots()
    ax.invert_yaxis()
    ax.set_xlabel('Nr. of visits')
    ax.set_title('Number of visits per day in the last %d days.\n This histogram is meant to display consistency.' % (days))

    # set figure variables
    ax.barh(ar_sites, instances, align='center', color="#247ba0")

    # show plot
    plt.rcdefaults()
    plt.show()