import re
import requests
from urllib.parse import urlparse, unquote

def get_html_google_maps(url: str):
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def extract_staticmap_url(html: str):
    PATTERN = r'https://maps\.google\.com/maps/api/staticmap\?center=[^"&]+'
    match = re.search(PATTERN, html)
    if match:
        return match.group(0)
    return None


def coords_from_staticmap_text(text: str):
    """
    Extrae lat y lng desde cualquier texto que contenga:
    https://maps.google.com/maps/api/staticmap?center=LAT,LNG
    (incluyendo %2C)
    """
    # Decodificar por si viene con %2C
    text = unquote(text)

    # Buscar el patrón center=LAT,LNG
    match = re.search(r"center=(-?\d+\.\d+),(-?\d+\.\d+)", text)
    if match:
        lat = float(match.group(1))
        lng = float(match.group(2))
        return lat, lng

    return None

def get_coords(url: str):
    text = get_html_google_maps(url)
    link = extract_staticmap_url(text)
    lat, long = coords_from_staticmap_text(link)
    return lat, long

if __name__ == '__main__':
    lat, long  = get_coords("https://maps.app.goo.gl/4ha5CvTcSpXmSCLMA")