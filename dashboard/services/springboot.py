import requests
from django.conf import settings


def get_from_spring(path):
    url = f"{settings.SPRING_BOOT_BASE_URL}{path}"

    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def post_to_spring(path, data=None):
    url = f"{settings.SPRING_BOOT_BASE_URL}{path}"

    response = requests.post(
        url,
        json=data or {},
        timeout=10
    )

    response.raise_for_status()

    return response.json()