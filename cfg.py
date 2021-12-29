from json import dumps
user_token = 'user token here' # защита будущая

proxy = None # прокси
requests_payload = {"number":1,"productId":170778093912111104} # для покупки боксов
product_id = 18394993  # для аукциона
saleTime = 1640689198 # время сейла в unix
requestsNumber = 1000 # количество запросов

def get_values():
    return {
        'user_token': user_token,
        'proxy': proxy,
        'requests_payload': requests_payload if isinstance(requests_payload, str)
                                             else dumps(requests_payload),  # noqa: E131
        'product_id': product_id
    }
