import requests

res = requests.get('https://jsonplaceholder.typicode.com/posts')
resp = res.json()
new_dicts = []
for dict_in_resp in resp:
    new = {}
    for k, v in dict_in_resp.items():
        if k in ['id', 'title']:
            new[k] = v
    new_dicts.append(new)

    # new_dict.pop('userId')
    # new_dict.pop('body')
