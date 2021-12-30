from json import dumps
user_token = 'user token here' # защита будущая
f=open("conf.cazakhBot", "r")
contents = list(map(int, f.read().strip().split(' ')))
f.close()
proxy = None # прокси
requests_payload = {"number":contents[0],"productId":contents[1]} # для покупки боксов
product_id = contents[2]  # для аукциона
saleTime = contents[3] # время сейла в unix
requestsNumber = contents[4] # количество запросов
def get_values():
    return {
        'user_token': user_token,
        'proxy': proxy,
        'requests_payload': requests_payload if isinstance(requests_payload, str)
                                             else dumps(requests_payload),  # noqa: E131
        'product_id': product_id
    }
