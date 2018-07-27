import requests


cookie = ''
cookies = {}
for line in cookie.split(';'):
    if line.strip() == '':
        continue
    value = line.strip().split('=')
    k = value[0]
    v = '='.join(value[1:])
    cookies[k] = v


headers = {
        'Authorization': 'Basic ZWxhc3RpYzpjaGFuZ2VtZQ==',
}

domain = 'http://192.168.33.10:9200'
res = requests.get(domain, headers=headers)
print(res.json())
res = requests.post(domain + '/customer?pretty', headers=headers)
print(res.status_code)
