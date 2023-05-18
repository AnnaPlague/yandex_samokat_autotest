import configuration
import requests
import get_order_by_track_test


# Запрос на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)


# Запрос на получение заказа по номеру трека
def get_order_by_track(track):
    params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params=params)