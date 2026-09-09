import requests
from django.conf import settings


class CertificateAPIError(Exception):
    pass


def get_service_headers():
    """
    Return authentication headers for Django -> Spring Boot
    server-to-server communication.

    The service token is stored in the .env file as:
    DJANGO_SERVICE_TOKEN
    """

    token = getattr(settings, "DJANGO_SERVICE_TOKEN", None)

    if not token:
        raise CertificateAPIError(
            "DJANGO_SERVICE_TOKEN is not configured."
        )

    return {
        "Authorization": f"Bearer {token}",
    }


def verify_certificate(certificate_id):
    """
    Verify a certificate using Sudip's Spring Boot backend.

    Endpoint:
    GET /api/auth/cert-verification/{certificate_id}/verify
    """

    certificate_id = certificate_id.strip()

    if not certificate_id:
        raise CertificateAPIError(
            "Certificate ID cannot be empty."
        )

    url = (
        f"{settings.SPRING_BOOT_BASE_URL}"
        f"/api/auth/cert-verification/"
        f"{certificate_id}/verify"
    )

    headers = get_service_headers()

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15,
        )

        response.raise_for_status()

    except requests.RequestException as exc:
        raise CertificateAPIError(
            "Could not verify certificate with KavachAR backend."
        ) from exc

    try:
        return response.json()

    except ValueError as exc:
        raise CertificateAPIError(
            "Backend returned an invalid verification response."
        ) from exc


def get_certificate_qr(certificate_id):
    """
    Retrieve the QR code for a certificate.

    Endpoint:
    GET /api/auth/cert-verification/{certificate_id}/qr
    """

    certificate_id = certificate_id.strip()

    if not certificate_id:
        raise CertificateAPIError(
            "Certificate ID cannot be empty."
        )

    url = (
        f"{settings.SPRING_BOOT_BASE_URL}"
        f"/api/auth/cert-verification/"
        f"{certificate_id}/qr"
    )

    headers = get_service_headers()

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15,
        )

        response.raise_for_status()

    except requests.RequestException as exc:
        raise CertificateAPIError(
            "Could not retrieve certificate QR code."
        ) from exc

    return response