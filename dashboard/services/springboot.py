import requests
from django.conf import settings


class SpringBootAPIError(Exception):
    pass


def get_service_headers():
    """
    Return authentication headers for Django -> Spring Boot
    server-to-server communication.
    """

    token = getattr(settings, "DJANGO_SERVICE_TOKEN", None)

    if not token:
        raise SpringBootAPIError(
            "DJANGO_SERVICE_TOKEN is not configured."
        )

    return {
        "Authorization": f"Bearer {token}",
    }


def get_from_spring(path):
    """
    Send a GET request to the Spring Boot backend
    using the Django service token.
    """

    url = f"{settings.SPRING_BOOT_BASE_URL}{path}"

    headers = get_service_headers()

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15,
        )

        response.raise_for_status()

    except requests.RequestException as exc:
        raise SpringBootAPIError(
            f"Could not connect to KavachAR backend: {exc}"
        ) from exc

    try:
        return response.json()

    except ValueError as exc:
        raise SpringBootAPIError(
            "Spring Boot backend returned an invalid JSON response."
        ) from exc


def post_to_spring(path, data=None):
    """
    Send a POST request to the Spring Boot backend
    using the Django service token.
    """

    url = f"{settings.SPRING_BOOT_BASE_URL}{path}"

    headers = get_service_headers()

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data or {},
            timeout=15,
        )

        response.raise_for_status()

    except requests.RequestException as exc:
        raise SpringBootAPIError(
            f"Could not connect to KavachAR backend: {exc}"
        ) from exc

    try:
        return response.json()

    except ValueError as exc:
        raise SpringBootAPIError(
            "Spring Boot backend returned an invalid JSON response."
        ) from exc