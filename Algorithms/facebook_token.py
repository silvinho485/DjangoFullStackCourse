import requests

proxies = {'http': 'socks5://127.0.0.1:9999',    'https': 'socks5://127.0.0.1:9999'}

data = {'access_token':'TOKEN VAI AQUI'}


def comidinia():
    cardapio = requests.get('https://graph.facebook.com/v2.12/delicia.arte.3/posts', proxies = proxies, params=data)
    # import pdb; pdb.set_trace()
    cardapioDoDia = cardapio.json().get("data")[0]['message']
    return cardapioDoDia
