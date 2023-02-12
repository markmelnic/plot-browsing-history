
import json, time
import numpy as np
from heapq import nlargest
from operator import itemgetter
import matplotlib.pyplot as plt
from urllib.parse import urlparse

from ignore import IGNORE

DAY = 86400000 # miliseconds

# generate plots
def generate_plots(data : list, size : int, days : int):
    # define figure
    fig, (links_plot, act_plot) = plt.subplots(2)
    fig.tight_layout()

    # LINKS PLOT
    links_plot.invert_yaxis()
    links_plot.set_xlabel('Number of visits')
    links_plot.set_title('Top %d most visited websites in the last %d days' % (size, days))
    # plot variables
    sorted_data = nlargest(size, data[0], key=itemgetter(1))
    sitenames = [el[0] for el in sorted_data]
    occurences = [el[1] for el in sorted_data]

    # set figure variables
    links_plot.barh(np.arange(len(sitenames)), occurences, align='center', color="#247ba0")
    links_plot.set_yticks(np.arange(len(sitenames)))
    links_plot.set_yticklabels(sitenames, minor=False)
    for ind, oc in enumerate(occurences):
        links_plot.text(oc + oc * 0.005, ind + .25, str(oc), color='#565656')

    # ACTIVITY PLOT
    act_plot.set_ylabel('Nr. of links visited')
    act_plot.set_xlabel('Nr. of days ago from today')
    act_plot.set_title('Number of links visited per day in the last %d days.\n This histogram is meant to display consistency.' % (days))
    # separate data
    days_ago = [el[0] for el in data[1]]
    instances = [el[1] for el in data[1]]
    act_plot.plot(np.arange(len(days_ago)), instances, label="Nr. of listings", color="#247ba0")

    # show plot
    plt.rcdefaults()
    plt.show()

# process json file
def chart_json(json_file : str, days : int) -> list:
    required_time = int(round(time.time() * 1000)) - (days * DAY)
    # read json file
    with open(json_file, mode = 'r', encoding="utf8") as data_file:
        data = json.load(data_file)

    sites = []
    instances = []
    # process data
    for data_set in data['Browser History']:
        #icon = data_set['favicon_url']
        timestamp = round(int(data_set['time_usec']) / 1000)
        if required_time > timestamp:
            continue

        url = data_set['url']
        try:
            url = urlparse(url).netloc.replace("www.", "")
        except AssertionError:
            continue

        if url not in sites:
            # index url
            sites.append(url)
            instances.append(1)
        else:
            # increment instance
            instances[sites.index(url)] += 1

    # merge url and instance to a tuple
    return [(site, inst) for site, inst in zip(sites, instances)]

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
