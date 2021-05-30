
import json
import os
from statistics import mean, median

import requests
from dotenv import load_dotenv

from queries import (get_all_attributes, get_all_name, get_one_attributes,
                     get_one_name)

load_dotenv()

# Get env variables
rest_url = os.getenv('API_URL')
graphql_url = '{}/graphql'.format(rest_url)
token = 'Bearer {}'.format(os.getenv('AUTH_TOKEN'))

repeat_times = 10

# the tuples items are respectively the size and time taken
results = {
    'single_user': {
        'rest': {
            'name': (0, 0),
            'attributes': (0, 0)
        },
        'graphql': {
            'name': (0, 0),
            'attributes': (0, 0)
        },
    },
    '100_users': {
        'rest': {
            'name': (0, 0),
            'attributes': (0, 0)
        },
        'graphql': {
            'name': (0, 0),
            'attributes': (0, 0)
        },
    }
}


# get single user name with REST
time = []
size = []
for i in range(repeat_times):
    response = requests.get('{}/users/torvalds'.format(rest_url), headers={
        'Authorization': token
    })

    time.append(response.elapsed.total_seconds() * 1000)
    size.append(len(response.content))

    response.raise_for_status()

results['single_user']['rest']['name'] = int(mean(time)), median(size)

# get single user name with GraphQL
time = []
size = []
for i in range(repeat_times):
    response = requests.post(
        graphql_url,
        json={'query': get_one_name()},
        headers={
            'Authorization': token
        }
    )

    time.append(response.elapsed.total_seconds() * 1000)
    size.append(len(response.content))

    response.raise_for_status()

results['single_user']['graphql']['name'] = int(mean(time)), median(size)

# get 100 users names with REST
time = []
size = []
for i in range(repeat_times):
    response = requests.get('{}/users?per_page=100'.format(rest_url), headers={
        'Authorization': token
    })

    time.append(response.elapsed.total_seconds() * 1000)
    size.append(len(response.content))

    response.raise_for_status()

results['100_users']['rest']['name'] = int(mean(time)), median(size)

# get 100 users names with GraphQL
time = []
size = []
for i in range(repeat_times):
    response = requests.post(
        graphql_url,
        json={'query': get_all_name()},
        headers={
            'Authorization': token
        }
    )

    time.append(response.elapsed.total_seconds() * 1000)
    size.append(len(response.content))

    response.raise_for_status()

results['100_users']['graphql']['name'] = int(mean(time)), median(size)

# get single user attributes with REST
time = []
size = []
for i in range(repeat_times):
    response = requests.get('{}/users/torvalds'.format(rest_url), headers={
        'Authorization': token
    })

    time.append(response.elapsed.total_seconds() * 1000)
    size.append(len(response.content))

    response.raise_for_status()

results['single_user']['rest']['attributes'] = int(mean(time)), median(size)

# get single user attributes with GraphQL
time = []
size = []
for i in range(repeat_times):
    response = requests.post(
        graphql_url,
        json={'query': get_one_attributes()},
        headers={
            'Authorization': token
        }
    )

    time.append(response.elapsed.total_seconds() * 1000)
    size.append(len(response.content))

    response.raise_for_status()

results['single_user']['graphql']['attributes'] = int(mean(time)), median(size)

# get 100 users attributes with REST
time = []
size = []
for i in range(repeat_times):
    response = requests.get('{}/users?per_page=100'.format(rest_url), headers={
        'Authorization': token
    })

    time.append(response.elapsed.total_seconds() * 1000)
    size.append(len(response.content))

    response.raise_for_status()

results['100_users']['rest']['attributes'] = int(mean(time)), median(size)

# get 100 users attributes with GraphQL
time = []
size = []
for i in range(repeat_times):
    response = requests.post(
        graphql_url,
        json={'query': get_all_attributes()},
        headers={
            'Authorization': token
        }
    )

    time.append(response.elapsed.total_seconds() * 1000)
    size.append(len(response.content))

    response.raise_for_status()

results['100_users']['graphql']['attributes'] = int(mean(time)), median(size)


# print results into file
with open('result.json', 'w+') as file:
    json.dump(results, file, indent=2)
