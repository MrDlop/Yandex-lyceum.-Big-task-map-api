from io import BytesIO
import requests


def params(coords: int, scale: int = 2) -> BytesIO:
    '''
    :param coords: object coordinates
    :param scale: scale image (1-4)
    :return: BytesIO map
    '''

    # map URL
    map_api_server = "http://static-maps.yandex.ru/1.x/"

    # params for search in static-maps
    map_params = {
        "ll": coords,
        "l": "map",
        "scale": str(scale)
    }

    # service call
    response = requests.get(map_api_server, params=map_params)

    return BytesIO(
        response.content)
