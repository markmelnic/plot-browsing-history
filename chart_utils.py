
import json
import time
import numpy as np
from heapq import nlargest
from operator import itemgetter
import matplotlib.pyplot as plt

DAY = 86400000 # miliseconds
from ignore import IGNORE

# process json file
def chart_json(json_file : str, days : int):
    
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
            url = url_formatter(url)
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
    merged_list = [(site, inst) for site, inst in zip(sites, instances)]

    return merged_list

# format the url to a standart format "url.TLD"
def url_formatter(url : str):

    # check if needs to be skipped
    for ign in IGNORE:
        assert (ign not in url)

    # remove string following TLD
    url = '/'.join(url.split('/')[:3])

    # subtract subdomains
    dot_index = [i for i, ltr in enumerate(url) if ltr == '.']
    if len(dot_index) > 1:
        url = url[: url.find('/') + 2] + url[dot_index[-2] + 1 :]

    # subtract port
    colon_index = [i for i, ltr in enumerate(url) if ltr == ':']
    if len(colon_index) > 1:
        url = url[: colon_index[-1]]

    # remove url protocol
    url = url.replace('http://', '').replace('https://', '')
    
    assert (len(url) > 3)
    return url

# generate chart
def generate_chart(data : list, size : int, days : int):

    # sort data
    sorted_data = nlargest(size, data, key=itemgetter(1))
    
    # plot variables
    sitenames = [el[0] for el in sorted_data]
    occurences = [el[1] for el in sorted_data]
    ar_sites = np.arange(len(sitenames))

    # define figure
    fig, ax = plt.subplots()
    ax.invert_yaxis()
    ax.set_xlabel('Number of visits')
    ax.set_title('Top %d most visited websites in the last %d days' % (size, days))

    # set figure variables
    ax.barh(ar_sites, occurences, align='center', color="#247ba0")
    ax.set_yticks(ar_sites)
    ax.set_yticklabels(sitenames, minor=False)
    for ind, oc in enumerate(occurences):
        ax.text(oc + oc * 0.005, ind + .25, str(oc), color='#565656')

    # show plot
    plt.rcdefaults()
    plt.show()
