from io import BytesIO
import requests
from typing import Tuple


def map_for_coords(coords: Tuple[float, float],
                   scale: float = 2,
                   type_map: str = "sat",
                   **kwargs):
    """
    :param coords: object coordinates (x, y)
    :param scale: scale image (1-4)
    :param type_map: map/sat/skl/trf
    :param kwargs: other param for static-maps
    :return: BytesIO map
    """

    # search map URL
    map_api_server = "https://static-maps.yandex.ru/1.x/"

    # params for search in static-maps
    map_params = {
        "ll": ','.join(str(i) for i in coords),
        "l": type_map,
        "scale": str(scale)
    }
    for i in kwargs:
        map_params[i] = kwargs[i]

    # service call
    response = requests.get(map_api_server, params=map_params)

    return response


def search_name(obj: str) -> Tuple[float, float]:
    """
    :param obj: name object (for example: "Уфа")
    :return: coords object
    """

    # search map URL
    geocoder_api_server = "https://geocode-maps.yandex.ru/1.x/"

    # params for search in geocode-maps
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": obj,
        "format": "json"}

    # service call
    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()

    # cut json response
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    return toponym['Point']['pos']


def toponym_obj(obj: str) -> dict:
    """
    :param obj: object
    :return: toponym object
    """
    geocoder_api_server = "https://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": obj,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    return toponym


def address_obj(obj: str) -> str:
    """
    :param obj: object
    :return: full formatted address
    """
    toponym = toponym_obj(obj)
    return toponym['metaDataProperty']['GeocoderMetaData']['Address']['formatted']


def postal_number_obj(obj: str) -> str:
    """
    :param obj: object
    :return: postal number address
    """
    toponym = toponym_obj(obj)
    return toponym['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
