import sender_stand_request
import data


# Запрос на сохранение трека заказа
def save_order_track():
    response = sender_stand_request.post_new_order(data.order_body)
    return response.json().get('track')


# Проверка, что код ответа - 200
def test_get_order_by_track():
    track = save_order_track()
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200
