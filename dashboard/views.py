from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

import base64

from .services.springboot import get_from_spring
from .services.certificate_api import (
    CertificateAPIError,
    verify_certificate,
    get_certificate_qr,
)


# ============================================================
# ADMIN ACCESS
# ============================================================

def admin_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not (request.user.is_staff or request.user.is_superuser):
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper


class AdminLoginView(LoginView):
    template_name = "dashboard/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()

        if not (user.is_staff or user.is_superuser):
            form.add_error(
                None,
                "You are not authorized to access the admin panel."
            )
            return self.form_invalid(form)

        login(self.request, user)

        return redirect("admin-dashboard")


# ============================================================
# DASHBOARD
# ============================================================

@admin_required
def dashboard_view(request):
    data = {
        "total_workers": 248,
        "active_workers": 210,
        "completed_training": 192,
        "certificates_issued": 156,
        "certificates_pending": 12,
        "average_score": 84.5,
    }

    return render(
        request,
        "dashboard/dashboard.html",
            data
        
    )


# ============================================================
# WORKERS
# ============================================================

@admin_required
def workers_view(request):
    workers = [
        {
            "workerId": "W001",
            "name": "Rahul Kumar",
            "phone": "9876543210",
            "organization": "KavachAR Industries",
            "progress": 90,
            "status": "Active",
        },
        {
            "workerId": "W002",
            "name": "Amit Singh",
            "phone": "9876543211",
            "organization": "KavachAR Industries",
            "progress": 75,
            "status": "Active",
        },
        {
            "workerId": "W003",
            "name": "Sunita Devi",
            "phone": "9876543212",
            "organization": "KavachAR Industries",
            "progress": 100,
            "status": "Completed",
        },
    ]

    return render(
        request,
        "workers/workers.html",
        {
            "workers": workers
        }
    )


@admin_required
def worker_detail_view(request, worker_id):
    workers = {
        "W001": {
            "workerId": "W001",
            "name": "Rahul Kumar",
            "phone": "9876543210",
            "organization": "KavachAR Industries",
            "progress": 90,
            "status": "Active",
        },
        "W002": {
            "workerId": "W002",
            "name": "Amit Singh",
            "phone": "9876543211",
            "organization": "KavachAR Industries",
            "progress": 75,
            "status": "Active",
        },
        "W003": {
            "workerId": "W003",
            "name": "Sunita Devi",
            "phone": "9876543212",
            "organization": "KavachAR Industries",
            "progress": 100,
            "status": "Completed",
        },
    }

    attempts = {
        "W001": [
            {
                "moduleTitle": "Fire Safety",
                "score": 92,
                "status": "Passed",
                "date": "02 Sep 2026",
            },
            {
                "moduleTitle": "PPE Safety",
                "score": 78,
                "status": "Passed",
                "date": "03 Sep 2026",
            },
            {
                "moduleTitle": "Emergency Response",
                "score": 65,
                "status": "Failed",
                "date": "04 Sep 2026",
            },
        ],
        "W002": [
            {
                "moduleTitle": "Fire Safety",
                "score": 88,
                "status": "Passed",
                "date": "01 Sep 2026",
            },
            {
                "moduleTitle": "PPE Safety",
                "score": 81,
                "status": "Passed",
                "date": "03 Sep 2026",
            },
        ],
        "W003": [
            {
                "moduleTitle": "Fire Safety",
                "score": 96,
                "status": "Passed",
                "date": "28 Aug 2026",
            },
            {
                "moduleTitle": "Emergency Response",
                "score": 94,
                "status": "Passed",
                "date": "30 Aug 2026",
            },
        ],
    }

    certificates = {
        "W001": [
            {
                "certificateId": "KVR-2C1F3D5DBA7145C98E92A5C427A455E3",
                "moduleTitle": "Fire Safety",
                "score": 92,
                "status": "Pending",
            },
        ],
        "W002": [
            {
                "certificateId": "CERT002",
                "moduleTitle": "PPE Safety",
                "score": 85,
                "status": "Pending",
            },
        ],
        "W003": [
            {
                "certificateId": "CERT003",
                "moduleTitle": "Emergency Response",
                "score": 96,
                "status": "Verified",
            },
        ],
    }

    worker = workers.get(
        worker_id,
        {
            "workerId": worker_id,
            "name": "Unknown Worker",
            "phone": "N/A",
            "organization": "N/A",
            "progress": 0,
            "status": "Unknown",
        },
    )

    worker_attempts = attempts.get(worker_id, [])
    worker_certificates = certificates.get(worker_id, [])

    return render(
        request,
        "workers/worker_detail.html",
        {
            "worker": worker,
            "attempts": worker_attempts,
            "certificates": worker_certificates,
        },
    )


# ============================================================
# CERTIFICATES
# ============================================================

@admin_required
def certificates_view(request):
    """
    Get ALL certificates from the Spring Boot backend.

    Spring Boot endpoint:
    GET /api/auth/cert-verification/certificates

    The backend returns a list like:

    [
        {
            "certificateId": "...",
            "userId": "...",
            "recipientName": "...",
            "certificateTitle": "...",
            "issuedAt": "...",
            "verificationUrl": "...",
            "status": "VALID"
        }
    ]

    No certificate IDs are hard-coded here.
    """

    try:
        certificates = get_from_spring(
            "/api/auth/cert-verification/certificates"
        )

        # The endpoint currently returns a JSON list.
        if not isinstance(certificates, list):
            certificates = []

    except Exception as exc:
        messages.error(
            request,
            f"Could not load certificates: {exc}"
        )
        certificates = []

    return render(
        request,
        "certificates/certificates.html",
        {
            "certificates": certificates
        },
    )


@admin_required
def certificate_detail_view(request, certificate_id):
    """
    Display details of one certificate.

    IMPORTANT:
    The certificate ID comes from the certificates list returned
    by Spring Boot. It is NOT hard-coded.

    We first load all certificates and find the matching certificate.
    This avoids assuming that a separate
    /certificates/{certificate_id} endpoint exists.
    """

    try:
        certificates = get_from_spring(
            "/api/auth/cert-verification/certificates"
        )

        if not isinstance(certificates, list):
            certificates = []

    except Exception as exc:
        messages.error(
            request,
            f"Could not load certificates: {exc}"
        )
        return redirect("certificates")

    certificate = None

    for item in certificates:
        if item.get("certificateId") == certificate_id:
            certificate = item
            break

    if certificate is None:
        messages.error(
            request,
            "Certificate not found."
        )
        return redirect("certificates")

    return render(
        request,
        "certificates/certificate_detail.html",
        {
            "certificate": certificate
        },
    )


# ============================================================
# VERIFY CERTIFICATE
# ============================================================

@admin_required
@require_POST
def verify_certificate_view(request, certificate_id):
    """
    Verify a certificate using the Spring Boot backend.

    Endpoint used by the service layer:

    GET /api/auth/cert-verification/{certificate_id}/verify

    If the certificate is valid, retrieve its QR code as well.
    """

    try:
        # ----------------------------------------------------
        # STEP 1: VERIFY CERTIFICATE
        # ----------------------------------------------------

        verification_result = verify_certificate(
            certificate_id
        )

        if not isinstance(verification_result, dict):
            messages.error(
                request,
                "Invalid response received from the backend."
            )

            return redirect(
                "certificate-detail",
                certificate_id=certificate_id,
            )

        # ----------------------------------------------------
        # STEP 2: CHECK VALIDITY
        # ----------------------------------------------------

        if not verification_result.get("valid", False):

            messages.error(
                request,
                "Certificate is INVALID."
            )

            return redirect(
                "certificate-detail",
                certificate_id=certificate_id,
            )

        # ----------------------------------------------------
        # STEP 3: GET QR CODE
        # ----------------------------------------------------

        qr_response = get_certificate_qr(
            certificate_id
        )

        qr_base64 = base64.b64encode(
            qr_response.content
        ).decode("utf-8")

        # ----------------------------------------------------
        # STEP 4: DISPLAY VERIFIED CERTIFICATE + QR
        # ----------------------------------------------------

        return render(
            request,
            "certificates/certificate.html",
            {
                "certificate": verification_result,
                "qr_base64": qr_base64,
            },
        )

    except CertificateAPIError as exc:

        messages.error(
            request,
            str(exc)
        )

        return redirect(
            "certificate-detail",
            certificate_id=certificate_id,
        )


# ============================================================
# ANALYTICS
# ============================================================

@admin_required
def analytics_view(request):
    analytics = {
        "total_workers": 248,
        "active_workers": 210,
        "completed_training": 192,
        "certificates_issued": 156,
        "certificates_pending": 12,
        "average_score": 84.5,
        "passed_attempts": 205,
        "failed_attempts": 43,
        "completion_rate": 77.4,
    }

    return render(
        request,
        "analytics/analytics.html",
        {
            "analytics": analytics
        },
    )


# ============================================================
# PROFILE
# ============================================================

@admin_required
def profile_view(request):
    return render(
        request,
        "profile/profile.html",
        {
            "admin": request.user
        },
    )