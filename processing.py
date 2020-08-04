
import sys
import json

# to be skipped
skipped = ['chrome://newtab', 'view-source']

# read json file
with open(sys.argv[1], mode = 'r', encoding="utf8") as json_file:
    data = json.load(json_file)

sites = []
instances = []
# process data
for data_set in data['Browser History']:
    #icon = data_set['favicon_url']
    url = '/'.join(data_set['url'].split('/')[:3])
    # check if needs to be skipped
    for el in skipped:
        if el in url:
            continue
        
    # format url to fit standarts
    point_index = [i for i, ltr in enumerate(url) if ltr == '.']
    if len(point_index) > 1:
        url = url[0 : url.find('/') + 2] + url[point_index[-2] + 1 :]
    
    # append to lists
    if url not in sites:
        sites.append(url)
        instances.append(1)
    else:
        instances[sites.index(url)] += 1


for i, site in zip(instances, sites):
    print(i, site)