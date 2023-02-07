from io import BytesIO
import requests


def map_for_coords(coords: list[float, float],
                   scale: float = 2,
                   type_map: str = "map",
                   **kwargs) -> BytesIO:
    """
    :param coords: object coordinates [x, y]
    :param scale: scale image (1-4)
    :param type_map: map/sat/skl/trf
    :param kwargs: other param for static-maps
    :return: BytesIO map
    """

    # search map URL
    map_api_server = "http://static-maps.yandex.ru/1.x/"

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

    return BytesIO(
        response.content)


def search_name(obj: str,
                scale: float = 2,
                type_map: str = "map") -> BytesIO:
    """
    :param type_map: map/sat/skl/trf
    :param scale: scale image (1-4)
    :param obj: name object (for example: "Уфа")
    :return: BytesIO map
    """

    # search map URL
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

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
    # coords center
    toponym_coodrinates = toponym["Point"]["pos"]
    # latitude and longitude
    toponym_longitude, toponym_latitude = toponym_coodrinates.split(" ")

    tp = [list(map(float, toponym['boundedBy']['Envelope'][i].split())) for i in toponym['boundedBy']['Envelope']]
    dx = str(abs(tp[0][0] - tp[1][0]))
    dy = str(abs(tp[0][1] - tp[1][1]))

    # # params for search in static-maps
    map_params = {
        "spn": ",".join([dx, dy]),
        "pt": f"{toponym['Point']['pos'].replace(' ', ',')},round"
    }

    return map_for_coords([toponym_longitude, toponym_latitude],
                          scale=scale,
                          type_map=type_map,
                          **map_params)
