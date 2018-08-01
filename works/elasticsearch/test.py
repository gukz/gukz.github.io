import requests
import json


cookie = ''
cookies = {}
for line in cookie.split(';'):
    if line.strip() == '':
        continue
    value = line.strip().split('=')
    k = value[0]
    v = '='.join(value[1:])
    cookies[k] = v

headers = {'Authorization': 'Basic ZWxhc3RpYzpjaGFuZ2VtZQ=='}

domain = 'http://192.168.33.10:9200'
res = requests.get(domain, headers=headers)
data = {
    'user_id': 1,
    'first_name': 'john',
    'last_name': 'Smith',
    'age': 24,
    'about': 'i love to go rock climbing',
    'interests': ['sports', 'music']
}
res = requests.put(domain+'/megacorp/employee/{}'.format(data['user_id']),
                   data=json.dumps(data), headers=headers)
data.update(user_id=2, first_name='tom', about='enjoy swimming', age=50)
res = requests.put(domain+'/megacorp/employee/{}'.format(data['user_id']),
                   data=json.dumps(data), headers=headers)
data.update(user_id=3, last_name='whalter', about='i enjoy rock mountain')
res = requests.put(domain+'/megacorp/employee/{}'.format(data['user_id']),
                   data=json.dumps(data), headers=headers)

query = {
    'query': {
        'match': {
            'last_name': 'Smith'
        }
    }
}
res = requests.get(domain+'/megacorp/employee/_search', data=json.dumps(query),
                   headers=headers)
print('\nquery last_name Smith\n', res.json())
query = {
    'query': {
        'bool': {
            'must': {
                'match': {
                    'last_name': 'smith'
                }
            },
            'filter': {
                'range': {
                    'age': {'gt': 40}
                }
            }
        }
    }
}
res = requests.get(domain+'/megacorp/employee/_search', data=json.dumps(query),
                   headers=headers)
print('\nquery last_name smith and age > 40\n', res.json())
query = {
    'query': {
        'match': {
            'about': 'rock climbing'
        }
    }
}
res = requests.get(domain+'/megacorp/employee/_search', data=json.dumps(query),
                   headers=headers)
print('\nquery those enjoy climbing\n', res.json())
query = {
    'query': {
        'match_phrase': {
            'about': 'rock climbing'
        }
    }
}
res = requests.get(domain+'/megacorp/employee/_search', data=json.dumps(query),
                   headers=headers)
print('\nmatch_phrase query with rock climbing\n', res.json())
query = {
    'query': {
        'match_phrase': {
            'about': 'rock climbing'
        }
    },
    'highlight': {
        'fields': {
            'about': {}
        }
    }
}
res = requests.get(domain+'/megacorp/employee/_search', data=json.dumps(query),
                   headers=headers)
print('\nmatch_phrase with highlight query rock climbing\n', res.json())
mapping = {
    'properties': {
        'interests': {
            'type': 'text',
            'fielddata': True}}}
res = requests.put(domain+'/megacorp/_mapping/employee/',
                   data=json.dumps(mapping), headers=headers)
print('\nmapping interests to fielddata: \n', res.json())
query = {
    'aggs': {
        'all_interests': {
            'terms': {'field': 'interests'}
        }
    }
}
res = requests.get(domain+'/megacorp/employee/_search', data=json.dumps(query),
                   headers=headers)
print('\naggregations query interests\n', res.json())
query = {
    'aggs': {
        'all_interests': {
            'terms': {'field': 'interests'}
        }
    },
    'query': {
        'match': {
            'last_name': 'smith'
        }
    }
}
res = requests.get(domain+'/megacorp/employee/_search', data=json.dumps(query),
                   headers=headers)
print('\naggregations query interests and query last_name\n', res.json())
query = {
    'aggs': {
        'all_interests': {
            'terms': {'field': 'interests'},
            'aggs': {
                'avg_age': {
                    'avg': {'field': 'age'}
                }
            }
        }
    },
    'query': {
        'match': {
            'last_name': 'smith'
        }
    }
}
res = requests.get(domain+'/megacorp/employee/_search', data=json.dumps(query),
                   headers=headers)
print('\naggregations query interests and query last_name and averate age\n',
      res.json())
